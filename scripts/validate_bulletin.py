#!/usr/bin/env python3
import os
import re
import sys
import urllib.request
import pdfplumber
import bs4

def get_latest_bulletins(bulletins_dir):
    if not os.path.exists(bulletins_dir):
        print(f"Error: Bulletins directory '{bulletins_dir}' does not exist.")
        sys.exit(1)
    
    files = [f for f in os.listdir(bulletins_dir) if re.match(r'^\d{4}-\d{2}-\d{2}\.html$', f)]
    files.sort(reverse=True)
    
    if len(files) < 2:
        print("Warning: Less than two bulletin HTML files found. Skipping comparative checks.")
        return files[0] if files else None, None
    
    return files[0], files[1]

def clean_html(element):
    if not element:
        return ""
    # Normalize whitespaces and convert to string
    return re.sub(r'\s+', ' ', str(element)).strip()

def verify_static_blocks(current_path, previous_path, template_path):
    print("--- Checking Static Blocks Consistency ---")
    
    current_info = extract_element(current_path, ".church-info")
    prev_info = extract_element(previous_path, ".church-info")
    temp_info = extract_element(template_path, ".church-info")
    
    current_mass = extract_element(current_path, ".mass-table")
    prev_mass = extract_element(previous_path, ".mass-table")
    temp_mass = extract_element(template_path, ".mass-table")
    
    errors = 0
    
    # 1. Church Info Verification
    if current_info != temp_info:
        print("[FAIL] Current church-info block does not match master_template.html exactly.")
        errors += 1
    if previous_path and current_info != prev_info:
        print("[FAIL] Current church-info block does not match previous week's HTML.")
        errors += 1
    if errors == 0:
        print("[PASS] Church information block is consistent.")
        
    mass_errors = 0
    # 2. Mass Table Verification
    if current_mass != temp_mass:
        print("[FAIL] Current mass-table schedule does not match master_template.html exactly.")
        mass_errors += 1
    if previous_path and current_mass != prev_mass:
        print("[FAIL] Current mass-table schedule does not match previous week's HTML.")
        mass_errors += 1
    if mass_errors == 0:
        print("[PASS] Mass & Devotions schedule table is consistent.")
        
    return errors + mass_errors

def extract_element(file_path, selector):
    if not file_path or not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')
    return clean_html(soup.select_one(selector))

def extract_pdf_text(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += (page.extract_text() or "") + "\n"
    except Exception as e:
        print(f"Error reading PDF {pdf_path}: {e}")
    return text

def download_file(url, dest):
    try:
        print(f"Downloading previous Korean PDF from: {url}")
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
        )
        with urllib.request.urlopen(req) as response, open(dest, 'wb') as out_file:
            out_file.write(response.read())
        return True
    except Exception as e:
        print(f"Failed to download previous PDF: {e}")
        return False

def get_pdf_link_from_html(html_path):
    if not os.path.exists(html_path):
        return None
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')
    link_elem = soup.select_one(".korean-link-bar a")
    return link_elem['href'] if link_elem and 'href' in link_elem.attrs else None

def get_announcement_block(html_path, keyword):
    if not os.path.exists(html_path):
        return None
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')
    blocks = soup.select(".announcement")
    for block in blocks:
        if keyword.lower() in block.get_text().lower():
            return clean_html(block)
    return None

def verify_announcements_consistency(current_html, previous_html, current_pdf, previous_pdf):
    print("\n--- Checking Announcement Translation Consistency ---")
    
    current_korean = extract_pdf_text(current_pdf)
    prev_korean = extract_pdf_text(previous_pdf)
    
    if not current_korean or not prev_korean:
        print("[WARNING] Could not retrieve PDF text. Skipping text alignment checks.")
        return 0
        
    KEYWORD_MAP = {
        "Confirmation": {"ko": ["견진"], "en": "Confirmation"},
        "RCIA": {"ko": ["예비 신자", "예비신자"], "en": "RCIA"},
        "UNITAS": {"ko": ["UNITAS", "unitas"], "en": "UNITAS"},
        "Soccer": {"ko": ["축구"], "en": "Soccer"},
        "Baby Bottle": {"ko": ["Baby Bottle", "Knights of Columbus"], "en": "Baby Bottle"},
        "Speaker Series": {"ko": ["Speaker", "oral surgery"], "en": "Speaker"},
        "Altar Servers": {"ko": ["복사단"], "en": "Altar"},
        "Stories": {"ko": ["이야기", "나눠주세요"], "en": "Stories"},
        "Soccer Gear": {"ko": ["Soccer Gear", "스포츠 용품"], "en": "Soccer Gear"},
        "Vacation": {"ko": ["사무장 휴가", "휴가"], "en": "Vacation"},
        "St. Mary": {"ko": ["성모회"], "en": "St. Mary"},
    }
    
    warnings = 0
    for name, keywords in KEYWORD_MAP.items():
        # Get current and previous Korean text snippets containing the keywords
        curr_snippets = [line.strip() for line in current_korean.split('\n') if any(k in line for k in keywords["ko"])]
        prev_snippets = [line.strip() for line in prev_korean.split('\n') if any(k in line for k in keywords["ko"])]
        
        curr_text_block = " ".join(curr_snippets)
        prev_text_block = " ".join(prev_snippets)
        
        # If the Korean announcement content is identical and not empty
        if curr_text_block and prev_text_block and curr_text_block == prev_text_block:
            # Check the corresponding English block in the HTML
            curr_en = get_announcement_block(current_html, keywords["en"])
            prev_en = get_announcement_block(previous_html, keywords["en"])
            
            if curr_en and prev_en and curr_en != prev_en:
                print(f"[FAIL] Announcement '{name}' has identical Korean text, but different English HTML translations:")
                print(f"  Current HTML:  {curr_en[:120]}...")
                print(f"  Previous HTML: {prev_en[:120]}...")
                warnings += 1
            elif curr_en and prev_en:
                print(f"[PASS] Announcement '{name}' translation is consistent with last week.")
                
    return warnings

def main():
    bulletins_dir = "docs/bulletins"
    template_path = "master_template.html"
    
    current_file, previous_file = get_latest_bulletins(bulletins_dir)
    if not current_file:
        print("No bulletins found.")
        sys.exit(1)
        
    current_html = os.path.join(bulletins_dir, current_file)
    previous_html = os.path.join(bulletins_dir, previous_file) if previous_file else None
    
    print(f"Current Weekly Bulletin: {current_html}")
    if previous_html:
        print(f"Previous Weekly Bulletin: {previous_html}")
        
    static_errors = verify_static_blocks(current_html, previous_html, template_path)
    
    translation_warnings = 0
    if previous_html:
        # Detect PDF paths
        current_date = current_file.replace(".html", "")
        previous_date = previous_file.replace(".html", "")
        
        current_pdf = f"{current_date}.pdf"
        previous_pdf = f"temp_extraction/{previous_date}.pdf"
        
        # Download PDFs if not exists
        os.makedirs("temp_extraction", exist_ok=True)
        if not os.path.exists(current_pdf):
            current_pdf_url = get_pdf_link_from_html(current_html)
            if current_pdf_url:
                download_file(current_pdf_url, current_pdf)
                
        if not os.path.exists(previous_pdf):
            pdf_url = get_pdf_link_from_html(previous_html)
            if pdf_url:
                download_file(pdf_url, previous_pdf)
                
        if os.path.exists(current_pdf) and os.path.exists(previous_pdf):
            translation_warnings = verify_announcements_consistency(
                current_html, previous_html, current_pdf, previous_pdf
            )
        else:
            print("[WARNING] Missing local or downloaded PDF files. Skipping comparative checks.")
            
    print("\n--- Validation Summary ---")
    print(f"Static block errors: {static_errors}")
    print(f"Translation inconsistencies: {translation_warnings}")
    
    if static_errors > 0 or translation_warnings > 0:
        print("\n[RESULT] Validation failed! Please fix the inconsistencies listed above.")
        sys.exit(1)
    else:
        print("\n[RESULT] Validation passed successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
