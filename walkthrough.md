# Weekly Bulletin Translation Job Walkthrough (July 5, 2026)

We have successfully executed the weekly bulletin translation and publishing job for **July 5, 2026**.

## Summary of Completed Work

1. **Retrieved the Latest Korean Bulletin**:
   - Downloaded the original bulletin PDF locally from `https://www.tvkcc.org/wp-content/uploads/2026/07/07052026_749.pdf`.

2. **Extracted Liturgical Info & Colors**:
   - Sunday Liturgical Title: **St. Andrew Kim Tae-gon, Priest and Martyr, Patron of the Korean Clergy - Devotional Mass**
   - Liturgical Color Class: `liturgical-red` (Patronal Feast/Martyrdom Red, based on background color extraction `(1.0, 0.0, 0.0)` from Page 1).

3. **Extracted Sunday School & Priest Schedule via OCR**:
   - Processed the Page 1 Priest Schedule image using macOS Vision OCR via a custom Swift script.
   - Captured the schedule and priest names:
     - 7/05: Sunday School N, Priest: Fr. Gerald
     - 7/12: Sunday School N, Priest: Fr. Jim
     - 7/19: Sunday School N, Priest: Fr. Philip
     - 7/26: Sunday School N, Priest: Fr. Paul
   - Prayer list: `윤정의 알퐁소, 이순옥 데레사, 김정희 데레사, 정종락 필립보, 배정례 엘리사벳, 이데이빗 바오로` (each wrapped in `<span>` tags with `&nbsp;` to prevent line break splits).

4. **Translated and Cataloged Announcements**:
   - Translated 7 announcements following the style guide and catalog templates:
     - **Establishment of the 8th Pastoral Council**: Translated the list of committee chairpersons and leaders of the new pastoral council (headed by President Joseph Hong).
     - **Parish Office Closure**: Translated the Cursillo and vacation schedule for the office manager.
     - **Sacrament of Confirmation, Confirmation Classes & Adult Education**: Class details, ceremony date, and online Google Form registration link.
     - **2026-2027 Sunday School Registration**: Guidelines for submitting applications and fees via Zelle/Venmo.
     - **Korean-American Catholic High School Summer Camp: Lifted**: Camp details with application deadline July 10, 2026.
     - **2026-2027 RCIA (Rite of Christian Initiation of Adults)**: Initiation scheduled for Easter Sunday (3/28/2027).
     - **30th Northern California Charismatic Conference**: Held on August 8, 2026.

5. **Updated Personnel in Header**:
   - Replaced the header personnel block in the bulletin page to reflect the new 8th Pastoral Council team:
     - **Pastor:** 오대석 바오로 신부 (925) 537-2909
     - **Pastoral Council Pres.:** 홍사현 요셉 (510) 676-6716
     - **Bereavement Society Pres.:** 박주암 레오폴드 (925) 852-1868

6. **Generated Output & Published**:
   - Saved the Markdown draft to [weekly_translation_draft_2026-07-05.md](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/drafts/weekly_translation_draft_2026-07-05.md).
   - Generated the styled HTML page at [2026-07-05.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-07-05.html).
   - Updated the navigation link on [2026-06-28.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-06-28.html) to link forward to July 5.
   - Updated the main archive page [index.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/index.html) (shifted `Latest` badge to July 5, added July 2026 section).
   - Cleaned up all temporary files inside `temp_extraction/`.
