# Weekly Bulletin Translation Job Walkthrough (July 12, 2026)

We have successfully executed the weekly bulletin translation and publishing job for **July 12, 2026**.

## Summary of Completed Work

1. **Retrieved the Latest Korean Bulletin**:
   - Downloaded the original bulletin PDF locally from `https://www.tvkcc.org/wp-content/uploads/2026/07/07122026_750.pdf`.

2. **Extracted Liturgical Info & Colors**:
   - Sunday Liturgical Title: **Fifteenth Sunday in Ordinary Time**
   - Liturgical Color Class: `liturgical-green` (Ordinary Time green, based on background color extraction `#38761d` from Page 1).

3. **Extracted Sunday School & Priest Schedule via OCR**:
   - Processed the Page 1 Priest Schedule image using macOS Vision OCR via a custom Swift script.
   - Captured the schedule and priest names:
     - 7/12: Sunday School N, Priest: Fr. Jim
     - 7/19: Sunday School N, Priest: Fr. Philip
     - 7/26: Sunday School N, Priest: Fr. Paul
     - 8/02: Sunday School N, Priest: TBA
   - Prayer list: `윤정의 알퐁소, 이순옥 데레사, 김정희 데레사, 정종락 필립보, 배정례 엘리사벳, 이데이빗 바오로` (each wrapped in `<span>` tags with `&nbsp;` to prevent line break splits).

4. **Translated and Cataloged Announcements**:
   - Translated 7 announcements following the style guide and catalog templates:
     - **Appointment of Finance Council**: Translated new chairperson (Gregory Hong) and members list.
     - **Parish Office Closure**: Outlined Cursillo and vacation dates for the office manager.
     - **Sacrament of Confirmation, Confirmation Classes & Adult Education**: Extended application deadline to July 19, updated liturgical rehearsal date to September 20.
     - **Share Your Stories!**: Added standard parish story contribution appeal.
     - **2026-2027 Sunday School Registration**: Guidelines for registrations and Zelle/Venmo payments.
     - **2026-2027 RCIA (Rite of Christian Initiation of Adults)**: Enrollment details for the new catechumen class starting in September.
     - **30th Northern California Charismatic Conference**: Held on August 8, 2026.

5. **Generated Output & Published**:
   - Saved the Markdown draft to [weekly_translation_draft_2026-07-12.md](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/drafts/weekly_translation_draft_2026-07-12.md).
   - Generated the styled HTML page at [2026-07-12.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-07-12.html).
   - Updated the navigation link on [2026-07-05.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-07-05.html) to link forward to July 12.
   - Updated the main archive page [index.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/index.html) (shifted `Latest` badge to July 12).
   - Run quality verification check script and verified it passed with 0 errors.
   - Cleaned up all temporary files inside `temp_extraction/`.
