# Weekly Bulletin Translation Job Walkthrough (June 28, 2026)

We have successfully executed the weekly bulletin translation and publishing job for **June 28, 2026**.

## Summary of Completed Work

1. **Retrieved the Latest Korean Bulletin**:
   - Downloaded the original bulletin PDF locally from `https://www.tvkcc.org/wp-content/uploads/2026/06/06282026_748.pdf`.

2. **Extracted Liturgical Info & Colors**:
   - Sunday Liturgical Title: **Thirteenth Sunday in Ordinary Time**
   - Liturgical Color Class: `liturgical-green` (Ordinary Time, based on background color extraction `#38761d` from Page 1).
   - Injected a `<style>` block in the head of the generated HTML to precisely override the title bar background color to `#38761d` (to match the exact green color from the Korean PDF).

3. **Extracted Sunday School & Priest Schedule via OCR**:
   - Processed the Page 1 Priest Schedule image using macOS Vision OCR via a custom Swift script.
   - Captured the schedule and priest names:
     - 6/28: Sunday School N, Priest: Fr. Paul
     - 7/05: Sunday School N, Priest: Fr. Gerald
     - 7/12: Sunday School N, Priest: Fr. Jim
     - 7/19: Sunday School N, Priest: Fr. Philip
   - Prayer list: `윤정의 알퐁소, 이순옥 데레사, 김정희 데레사, 정종락 필립보, 배정례 엘리사벳, 이데이빗 바오로` (each wrapped in `<span>` tags with `&nbsp;` to prevent line break splits).

4. **Translated and Cataloged Announcements**:
   - Translated 10 announcements following the style guide and catalog templates:
     - **Fr. Paul Dae-seok Oh's Patronal Feast Day**: Wished congratulations to the Pastor for his feast day on June 29.
     - **Fundraising for Ganggu Church**: Described the fundraiser, in-person offerings, and online payment details through Tithe.ly/Zelle.
     - **Sacrament of Confirmation, Confirmation Classes & Adult Education**: Extended application deadline to 7/12 (Sun).
     - **Sacrament Certificates & Photos Distribution**: Notified parishioners to pick up Easter/First Communion certificates.
     - **Gratitude to Outgoing Pastoral Council and Group Leaders**: Commended outgoing leaders for their two years of service.
     - **Korean-American Catholic High School Summer Camp: Lifted**: Outlined target, Y-camp location, Venmo payment details, and contacts.
     - **TVCS Annual Soccer Gear Drive**: Collection deadline 6/28 (Sun).
     - **2026-2027 RCIA (Rite of Christian Initiation of Adults)**: Initiation date 3/28/2027.
     - **30th Northern California Charismatic Conference**: Held on August 8, 2026.
     - **New Weekday Evening Mass**: Details on monthly first Wednesday evening mass.
   - **No Community Events**: Cleanly removed the optional Community Events section since none were scheduled in the Korean bulletin.

5. **Generated Output & Published**:
   - Saved the Markdown draft to [weekly_translation_draft_2026-06-28.md](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/drafts/weekly_translation_draft_2026-06-28.md).
   - Generated the styled HTML page at [2026-06-28.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-06-28.html).
   - Updated the navigation link on [2026-06-21.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-06-21.html) to link forward to June 28.
   - Updated the main archive page [index.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/index.html) (latest badge shifted to June 28).
   - Cleaned up all temporary files inside `temp_extraction/`.
