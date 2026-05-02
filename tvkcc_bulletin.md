# Antigravity Weekly Bulletin Workflow

**Description:** This file contains the strict instructions for the Antigravity Agent to execute the weekly translation of the TVKCC Korean bulletin into English and publish it as a styled HTML page.

**Trigger:** To run this workflow, the user will say: `@tvkcc_bulletin.md Execute the weekly bulletin translation.`

---

## 🤖 Agent Instructions

When the user triggers this workflow, execute the following steps in order:

### 1. Retrieve the Latest Bulletin
- Navigate to `https://www.tvkcc.org/weeklybulletins/`.
- Find the link to the most recent weekly bulletin (usually the first post).
- Open the post and extract the `.pdf` link for the bulletin.
- Download or read the contents of the PDF.

### 2. Retrieve Sunday Liturgy Title
- Determine the date of the upcoming Sunday.
- Go to `https://bible.usccb.org/` and find the English liturgy title for that Sunday (e.g., "Fifth Sunday of Easter").

### 3. Retrieve Pope's Monthly Prayer Intention
- Search for `Pope Francis prayer intention [Month] [Year]` to find the current month's intention.
- Extract the title and the full prayer text (both will be included in the HTML output).

### 4. Extract Key Sections
The Korean bulletin contains data across multiple pages. Extract ALL of the following:

**From Page 1:**
- **Mass & Sunday School Schedule (미사/주일학교)** — Korean Mass, English Mass, Sunday School, Weekday Mass, Confession, Holy Hour times
- **Priest & Parish Leadership** — Pastor, Pastoral Council President, Chief District Leader, Funeral Ministry Head with names and phone numbers
- **Sunday School & Priest Schedule Table** — Date, Sunday School (Y/N), Priest name for each upcoming week

**From the last page (공지사항 / Offertory):**
- **Liturgy Schedule & Key Dates (전례일정)** — translate EVERY detail including sub-notes under liturgy items (e.g., donation deadlines)
- **Community Events / Announcements (본당소식)** — translate EVERY detail
- **Offertory and Donations (감사헌금 및 교무금)** — all categories + donor lists
- **Prayer List (기도해 주십시오)**

### 5. Translate and Format
Translate the extracted sections from Korean to English. 
**CRITICAL:** You must format the translated output exactly according to the rules defined in `bulletin_style_guide.md`. 
**CRITICAL:** Before translating any Community Event/Announcement, you MUST check `bulletin_announcement_catalog.md`. If the announcement matches a template in the catalog, use that exact template and fill in the brackets.
- Ensure dates are formatted as `M/D (Day)`.
- Use standard markdown bullets (`*`) for all bullet points. Do NOT use Unicode characters like `●` or `◦` or dashes (`-`) — use asterisks (`*`) as they paste most cleanly into Google Docs as proper bullet dots.
- Use the standard keys: `Date/time:`, `Location:`, `Who:`, `Contact:`.
- Maintain Korean characters for names followed by baptismal names.

### 6. Output Generation — Markdown Draft
Create a new file named `~/Vibe/TVKCC Jubo/weekly_translation_draft_[YYYY-MM-DD].md` (using the upcoming Sunday's date) with the final translated text. Format the text inside the file into clean Markdown chunks:
- **Header**: Include the Date and the Liturgy Title (e.g., `May 3, 2026 - Fifth Sunday of Easter`) at the very top.
- **Chunk 1: Mass & Sunday School Schedule** (from page 1) and **Priest & Parish Leadership**
- **Chunk 2: Liturgy & Key Dates**
- **Chunk 3: Announcements**
- **Chunk 4: Offertory Numbers**

### 7. Output Generation — HTML Bulletin Page
Using the translated content, generate a styled HTML bulletin page at `~/Vibe/TVKCC Jubo/bulletins/[YYYY-MM-DD].html`.

Use `~/Vibe/TVKCC Jubo/bulletins/2026-05-03.html` as the **reference template**. Copy its exact HTML structure and CSS class names and replace the content with this week's data. Specifically:

1. **Banner & Header** — Update the liturgy title, date, and issue number in the title bar. Update the personnel names/numbers in the `<div class="header-personnel">` block if they have changed.
2. **Church Info Block** — This is static (address, phone, etc.) — keep as-is.
3. **Mass Schedule Table** — Update if any changes are mentioned in the bulletin (usually static). Ensure Devotions are formatted correctly.
4. **Leadership** — (Now part of Header)
5. **Liturgy & Key Dates** — Replace with this week's `<ul class="liturgy-list">` items. Include sub-notes using `<span class="sub-note">`.
6. **Community Events Table** — Replace table rows with this week's meetings.
7. **Announcements Grid** — Replace with this week's announcements in a two-column `<div class="announcements-grid">`. Use `<div class="announcement">` blocks with `<h3>` title and `<ul>` list. Balance left and right columns roughly equally.
8. **Offertory Table** — Update the amounts and donor lists.
9. **Pope's Prayer Intention** — Update the `<div class="pope-box">` with the current month's intention (title + prayer text).
10. **QR Code Block** — Keep as-is (static link to tvkcc.org/onlinegiving/).
11. **Schedule + Prayer Box** — Update the Sunday School/Priest schedule table and the "Please pray for" names list (located below the Mass table).
12. **Navigation links** — Add `← Previous Week` and `Next Week →` links in the footer pointing to the adjacent bulletin pages. Only show links for weeks that exist.
13. **Korean Bulletin Link** — Add a link to the original Korean PDF in the `<div class="korean-link-bar">` section.

After generating the HTML file, **update the index page** at `~/Vibe/TVKCC Jubo/index.html`:
- Add a new `<li>` entry at the TOP of the `<ul class="archive-list">` for the new bulletin (newest first).

### 8. Publish
Commit and push the new files to GitHub:
```bash
cd ~/Vibe/TVKCC\ Jubo
git add bulletins/[YYYY-MM-DD].html index.html weekly_translation_draft_[YYYY-MM-DD].md
git commit -m "Add weekly bulletin for [YYYY-MM-DD]"
git push
```

### 9. Open in Browser
After saving the file, use the `run_command` tool to automatically open the latest Korean PDF and the new HTML bulletin page on the user's Mac.
Run this command to explicitly open them in a brand new Google Chrome window with three tabs:
`open -n -a "Google Chrome" --args --new-window [URL to the latest Korean PDF] ~/Vibe/TVKCC\ Jubo/bulletins/[YYYY-MM-DD].html "https://drive.google.com/drive/folders/1xVZz_U6tnMSQjlmFU1zj0doT8-pCVDZS"`

### 10. Post-Translation Style Guide Update
After you have finished creating your English bulletin, if you made any manual style adjustments or added new announcement types, simply export it as a PDF and provide me (Antigravity) with the file path.
- I will parse your new English PDF, detect any new patterns or formatting changes you introduced, and automatically update the `bulletin_style_guide.md` to ensure I apply your new styles next week!
