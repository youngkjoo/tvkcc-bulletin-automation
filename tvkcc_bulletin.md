# Antigravity Weekly Bulletin Workflow

**Description:** This file contains the strict instructions for the Antigravity Agent to execute the weekly translation of the TVKCC Korean bulletin into English. 

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

### 3. Extract Key Sections
The Korean bulletin contains many pages, but we only care about specific sections (usually on the last page). Extract:
- **Liturgy Schedule (전례일정)**
- **Community Events / Announcements (본당소식)**
- **Offertory and Donations (감사헌금 및 교무금)**
- **Prayer List (기도해 주십시오)**
- **Priest Schedule (사제일정)**

### 4. Translate and Format
Translate the extracted sections from Korean to English. 
**CRITICAL:** You must format the translated output exactly according to the rules defined in `bulletin_style_guide.md`. 
**CRITICAL:** Before translating any Community Event/Announcement, you MUST check `bulletin_announcement_catalog.md`. If the announcement matches a template in the catalog, use that exact template and fill in the brackets.
- Ensure dates are formatted as `M/D (Day)`.
- Use standard markdown bullets (`-`) for all bullet points. Do NOT use Unicode characters like `●` or `◦` — these do not paste cleanly into Google Docs.
- Use the standard keys: `Date/time:`, `Location:`, `Who:`, `Contact:`.
- Maintain Korean characters for names followed by baptismal names.

### 5. Output Generation
Create a new file named `~/Vibe/TVKCC Jubo/weekly_translation_draft_[YYYY-MM-DD].md` (using the upcoming Sunday's date) with the final translated text. Format the text inside the file into clean Markdown chunks:
- **Header**: Include the Date and the Liturgy Title (e.g., `May 3, 2026 - Fifth Sunday of Easter`) at the very top.
- **Chunk 1: Liturgy Schedule**
- **Chunk 2: Announcements**
- **Chunk 3: Offertory Numbers**
- **Chunk 4: Priest Schedule & Prayers**

After saving the file, use the `run_command` tool to automatically open the latest Korean PDF and the new draft file on the user's Mac so they are immediately ready to work. 
Run this command to explicitly open them in a brand new Google Chrome window with three tabs:
`open -n -a "Google Chrome" --args --new-window [URL to the latest Korean PDF] ~/Vibe/TVKCC\ Jubo/weekly_translation_draft_[YYYY-MM-DD].md "https://drive.google.com/drive/folders/1xVZz_U6tnMSQjlmFU1zj0doT8-pCVDZS"`

### 6. Post-Translation Style Guide Update
After you have finished creating your English Google Doc, if you made any manual style adjustments or added new announcement types, simply export it as a PDF and provide me (Antigravity) with the file path.
- I will parse your new English PDF, detect any new patterns or formatting changes you introduced, and automatically update the `bulletin_style_guide.md` to ensure I apply your new styles next week!
