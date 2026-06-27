#!/usr/bin/env python3
import os
import sys
import re
import urllib.request
import json
import datetime
import argparse
from bs4 import BeautifulSoup
import pdfplumber

def call_gemini(api_key, system_instruction, prompt_text):
    # Endpoint for gemini-2.5-flash
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    
    payload = {
        "contents": [{
            "parts": [{
                "text": prompt_text
            }]
        }],
        "systemInstruction": {
            "parts": [{
                "text": system_instruction
            }]
        },
        "generationConfig": {
            "temperature": 0.1,
            "responseMimeType": "text/plain"
        }
    }
    
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            return res_data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print(f"Error calling Gemini API: {e}", file=sys.stderr)
        return None

def clean_markdown(text):
    if not text:
        return ""
    text = text.strip()
    if text.startswith("```markdown"):
        text = text[11:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()

def get_latest_bulletin_info():
    print("Scraping weekly bulletin list...")
    req = urllib.request.Request(
        "https://www.tvkcc.org/weeklybulletins/",
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    with urllib.request.urlopen(req) as response:
        soup = BeautifulSoup(response.read(), 'html.parser')
    
    article = soup.select_one(".blog_lists article")
    if not article:
        raise ValueError("Could not find article on weeklybulletins page")
    
    link_elem = article.select_one("h4 a")
    if not link_elem:
        raise ValueError("Could not find post link in article")
    
    post_url = link_elem['href']
    post_title = link_elem.get_text(strip=True)
    
    # Parse date from title: "연중 제13주일(교황 주일) / 6-28-2026(제748호)"
    date_match = re.search(r'(\d{1,2})-(\d{1,2})-(\d{4})', post_title)
    if not date_match:
        # Fallback check URL e.g. 06282026bulletin
        url_match = re.search(r'(\d{2})(\d{2})(\d{4})bulletin', post_url)
        if url_match:
            month, day, year = url_match.groups()
            date_str = f"{year}-{month}-{day}"
        else:
            raise ValueError(f"Could not parse date from title '{post_title}' or URL '{post_url}'")
    else:
        month, day, year = date_match.groups()
        date_str = f"{year}-{int(month):02d}-{int(day):02d}"
        
    return post_url, post_title, date_str

def get_pdf_link_from_post(post_url):
    print(f"Fetching post page: {post_url}")
    req = urllib.request.Request(
        post_url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    with urllib.request.urlopen(req) as response:
        soup = BeautifulSoup(response.read(), 'html.parser')
    
    for a in soup.select(".entry-content a"):
        href = a.get('href', '')
        if href.lower().endswith('.pdf'):
            return href
    raise ValueError(f"No PDF link found in post at {post_url}")

def download_file(url, dest):
    print(f"Downloading PDF from: {url} -> {dest}")
    req = urllib.request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    with urllib.request.urlopen(req) as response, open(dest, 'wb') as out_file:
        out_file.write(response.read())

def get_liturgy_title(sunday_date):
    date_str = sunday_date.strftime("%m%d%y")
    url = f"https://bible.usccb.org/bible/readings/{date_str}.cfm"
    print(f"Fetching liturgy title from USCCB: {url}")
    
    req = urllib.request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            soup = BeautifulSoup(response.read(), 'html.parser')
        meta_title = soup.find("meta", property="og:title")
        if meta_title and meta_title.get("content"):
            title = meta_title["content"].strip()
            print(f"Liturgy Title found: {title}")
            return title
    except Exception as e:
        print(f"Failed to fetch USCCB liturgy title for {sunday_date}: {e}", file=sys.stderr)
    return None

def extract_pdf_text(pdf_path):
    print(f"Extracting text from PDF: {pdf_path}")
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text += f"--- PAGE {i+1} ---\n"
            text += (page.extract_text() or "") + "\n"
    return text

def main():
    parser = argparse.ArgumentParser(description="Automate TVKCC Weekly Bulletin draft translation generation.")
    parser.add_argument("--date", help="Target Sunday date override (YYYY-MM-DD)")
    parser.add_argument("--force", action="store_true", help="Force run and overwrite existing draft")
    args = parser.parse_args()
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)
        
    try:
        # 1. Determine target date and PDF URL
        post_url, post_title, scraped_date = get_latest_bulletin_info()
        print(f"Scraped Date: {scraped_date}")
        print(f"Post Title: {post_title}")
        
        target_date_str = args.date if args.date else scraped_date
        print(f"Target Date: {target_date_str}")
        
        draft_path = f"drafts/weekly_translation_draft_{target_date_str}.md"
        if os.path.exists(draft_path) and not args.force:
            print(f"Draft for {target_date_str} already exists at {draft_path}. Skipping.")
            return
            
        pdf_url = get_pdf_link_from_post(post_url)
        local_pdf_path = f"{target_date_str}.pdf"
        
        # 2. Download PDF
        download_file(pdf_url, local_pdf_path)
        
        # 3. Get Liturgy Title
        sunday_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d")
        liturgy_title = get_liturgy_title(sunday_date)
        if not liturgy_title:
            # Fallback based on post title if usccb fails
            liturgy_title = "Sunday Liturgy"
            
        # 4. Extract PDF Text
        pdf_text = extract_pdf_text(local_pdf_path)
        
        # 5. Load assets
        if not os.path.exists("bulletin_style_guide.md"):
            print("Error: bulletin_style_guide.md not found in the root directory.", file=sys.stderr)
            sys.exit(1)
        if not os.path.exists("bulletin_announcement_catalog.md"):
            print("Error: bulletin_announcement_catalog.md not found in the root directory.", file=sys.stderr)
            sys.exit(1)
            
        with open("bulletin_style_guide.md", "r", encoding="utf-8") as f:
            style_guide = f.read()
            
        with open("bulletin_announcement_catalog.md", "r", encoding="utf-8") as f:
            catalog = f.read()
            
        # 6. Generate draft using Gemini
        system_instruction = (
            "You are an expert Korean-to-English translator for Catholic church bulletins. "
            "Your goal is to translate the Korean bulletin text into a structured English markdown draft. "
            "You must follow the TVKCC style guide and reuse templates from the catalog when matching announcements are found."
        )
        
        prompt = f"""
Target Date: {target_date_str}
USCCB Sunday Liturgy Title: {liturgy_title}

=== TVKCC STYLE GUIDE ===
{style_guide}

=== MASTER ANNOUNCEMENT CATALOG ===
{catalog}

=== EXTRACTED KOREAN BULLETIN TEXT ===
{pdf_text}

=== INSTRUCTIONS ===
1. Translate the extracted Korean bulletin text to English.
2. Structure the output as a Markdown file with clear sections matching:
   - Header (Liturgy Title and Date on the first line: `[Liturgy Title]  [M/D/YYYY]`)
   - Liturgy & Key Dates
   - Community Events / Announcements
   - Offertory and Donations (list of categories and donor names)
   - Sunday School & Priest Schedule Table (Date | Sunday School | Priest)
   - We Ask For Your Prayer (comma separated names)
   - Pope's Monthly Prayer Intention (both monthly theme/title and the prayer text)
3. For announcements, check the Master Announcement Catalog. If an announcement matches the intent, use that exact template and fill in the bracketed variables.
4. Keep names as: Korean name + Baptismal name (e.g. 장진환 라파엘).
5. Format all dates as M/D (Day), e.g. 6/28 (Sun).
6. Output ONLY the raw Markdown draft content. Do not include markdown code block backticks (```markdown) at the beginning or end. Output the text directly.
"""
        print("Translating with Gemini...")
        raw_draft = call_gemini(api_key, system_instruction, prompt)
        if not raw_draft:
            print("Error: Failed to generate draft from Gemini.", file=sys.stderr)
            sys.exit(1)
            
        clean_draft_content = clean_markdown(raw_draft)
        
        # Write draft file
        os.makedirs("drafts", exist_ok=True)
        with open(draft_path, "w", encoding="utf-8") as f:
            f.write(clean_draft_content)
            
        print(f"Success: Translation draft generated at {draft_path}")
        
    except Exception as e:
        print(f"Execution failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
