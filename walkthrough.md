# Weekly Bulletin Translation Job Walkthrough (July 19, 2026)

We have successfully executed the weekly bulletin translation and publishing job for **July 19, 2026**.

## Summary of Completed Work

1. **Retrieved the Latest Korean Bulletin**:
   - Processed the provided local/attached Korean PDF screenshots and OCR content since the weekly post was not yet uploaded to the official website.

2. **Extracted Liturgical Info & Colors**:
   - Sunday Liturgical Title: **Sixteenth Sunday in Ordinary Time**
   - Liturgical Color Class: `liturgical-green` (Ordinary Time green, based on background color extraction `#38761d` from Page 1).

3. **Extracted Sunday School & Priest Schedule via OCR**:
   - Analyzed the Page 1 schedule and names:
     - 7/19: Sunday School N, Priest: Fr. Philip
     - 7/26: Sunday School N, Priest: Fr. Paul
     - 8/02: Sunday School N, Priest: Fr. Paul (Updated from TBA)
     - 8/09: Sunday School N, Priest: Fr. Paul
   - Prayer list: `윤정의 알퐁소, 이순옥 데레사, 김정희 데레사, 정종락 필립보, 배정례 엘리사벳, 이데이빗 바오로` (each wrapped in `<span>` tags with `&nbsp;` to prevent line break splits).

4. **Translated and Cataloged Announcements**:
   - Translated 6 announcements following the style guide and catalog templates:
     - **Parish Office Closure**: Formatted with bold dates to match the Korean layout exactly.
     - **Sacrament of Confirmation, Confirmation Classes & Adult Education**: Re-verified class schedule and application deadline.
     - **2026-2027 Sunday School Registration**: Styled cleanly without extra headers.
     - **2026-2027 RCIA (Rite of Christian Initiation of Adults)**: Maintained consistency with historical translations.
     - **30th Northern California Charismatic Conference**: Held on August 8, 2026.
     - **Share Your Stories!**: Positioned as the final item in the right column, matching the layout.

5. **Generated Output & Published**:
   - Saved the Markdown draft to [weekly_translation_draft_2026-07-19.md](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/drafts/weekly_translation_draft_2026-07-19.md).
   - Generated the styled HTML page at [2026-07-19.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-07-19.html).
   - Updated the navigation link on [2026-07-12.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-07-12.html) to link forward to July 19.
   - Updated the main archive page [index.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/index.html) (shifted `Latest` badge to July 19).
   - Run quality verification script and verified it passed successfully.
