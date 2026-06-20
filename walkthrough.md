# Weekly Bulletin Translation Job Walkthrough (June 21, 2026)

We have successfully executed the weekly bulletin translation and publishing job for **June 21, 2026**.

## Summary of Completed Work

1. **Retrieved the Latest Korean Bulletin**:
   - Downloaded the original bulletin PDF locally from `https://www.tvkcc.org/wp-content/uploads/2026/06/06212026_747.pdf`.

2. **Extracted Liturgical Info & Colors**:
   - Sunday Liturgical Title: **Twelfth Sunday in Ordinary Time**
   - Liturgical Color Class: `liturgical-green` (Ordinary Time, based on background color extraction `#38761d` from Page 1).
   - Injected a `<style>` block in the head of the generated HTML to precisely override the title bar background color to `#38761d` (to match the exact green color from the Korean PDF).

3. **Extracted Sunday School & Priest Schedule via OCR**:
   - Processed the Page 1 Priest Schedule image using macOS Vision OCR via a custom Swift script.
   - Captured the schedule and corrected names:
     - 6/21: Sunday School N, Priest: Fr. Jim
     - 6/28: Sunday School N, Priest: Fr. Paul
     - 7/05: Sunday School N, Priest: Fr. Jim
     - 7/12: Sunday School N, Priest: Fr. Gerald
   - Prayer list: `윤정의 알퐁소, 이순옥 데레사, 김정희 데레사, 정종락 필립보, 배정례 엘리사벳, 이데이빗 바오로` (each wrapped in `<span>` tags with `&nbsp;` to prevent line break splits).

4. **Translated and Cataloged Announcements**:
   - Translated 9 announcements following the style guide and catalog templates (including *Father's Day Event*, *Sacrament of Confirmation*, *Lifted HS Summer Camp*, *RCIA*, *Charismatic Conference*, etc.).
   - Translated the new announcement about the **Weekday Evening Mass** (first Wednesday of the month at 7:30 PM).
   - Translated the new announcement about the **Catholic Bible Study Senior Reading Group** (Bible study for seniors, contact (925) 487-6055).
   - **Corrected Priest Name**: Updated the liturgy schedule to use **Fr. Franciscus Xaverius Park Hyo-jae** (formerly Fr. Hyojo Park F. Xavier) according to the official CBCK directory.
   - **Layout Alignment**: Rearranged the announcement columns to match the exact order of the original Korean bulletin (putting the *Senior Reading Group* notice at the bottom of the left column, and the *Italy Pilgrimage* notice in the right column between RCIA and the Charismatic Conference).

5. **Generated Output & Published**:
   - Saved the Markdown draft to [weekly_translation_draft_2026-06-21.md](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/drafts/weekly_translation_draft_2026-06-21.md).
   - Generated the styled HTML page at [2026-06-21.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-06-21.html).
   - Updated the navigation link on [2026-06-14.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-06-14.html) to link forward to June 21.
   - Updated the main archive page [index.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/index.html) (latest badge shifted to June 21).
   - Cleaned up all temporary files inside `temp_extraction/`.
