# Weekly Bulletin Translation Job Walkthrough (November 1, 2026)

We have successfully executed the weekly bulletin translation and publishing job for **November 1, 2026**.

## Summary of Completed Work

1. **Retrieved the Latest Korean Bulletin**:
   - Fetched the latest bulletin post directly from `https://www.tvkcc.org/weeklybulletins/` (Post: `모든 성인 대축일 / 11-1-2026(제766호)`).
   - Downloaded the official PDF from `https://www.tvkcc.org/wp-content/uploads/2026/10/11012026_766.pdf`.

2. **Extracted Liturgical Info & Colors**:
   - Sunday Liturgical Title: **Solemnity of All Saints** (No. 766).
   - Liturgical Color Class: `liturgical-white` (RGB `[0.9569, 0.8667, 0.7059]`, Hex `#f4ddb4`).

3. **Extracted Sunday School & Priest Schedule via Vision OCR & Extraction**:
   - Analyzed the Page 1 schedule table and prayer list:
     - 11/1: Sunday School Y, Priest: Fr. Gerald
     - 11/8: Sunday School Y, Priest: Fr. Paul
     - 11/15: Sunday School Y, Priest: Fr. Jim
     - 11/22: Sunday School N, Priest: Fr. Paul
   - Prayer list: `윤정의 알퐁소, 이순옥 데레사, 김정희 데레사, 정종락 필립보, 배정례 엘리사벳, 이데이빗 바오로, 이혁주 베드로, 이정수 비오, 권진주 마르가리타, 한규용 바오로, 한지아 클레어` (each wrapped in `<span>` tags with `&nbsp;` to prevent line break splits).

4. **Translated Community Events & Announcements**:
   - **Community Events (`모임 안내`)**:
     - Faith Community Leaders: 11/1 (Sun) 10:45 AM, Room A
     - Mother of Love Curia: 11/8 (Sun) 10:45 AM - 12:00 PM, Room A
     - Secular Franciscan Order: 11/8 (Sun) 1:00 PM, Room B
     - St. Mary's Society 2026 2nd Half General Assembly: 11/22 (Sun) 10:45 AM - 11:15 AM, Room A
   - **Announcements (9 items, balanced across two columns)**:
     - **Education Committee**: RCIA class inquiry (Sunday 11:00 AM – 12:00 PM in CCOP Office) and rosary/prayer book donations.
     - **TVCS Bake Sale Event Notice**: Today, 11/1 (Sun) after Mass in the Church vestibule for World Youth Day 2027 in Korea.
     - **St. Mary's Society Acorn Noodles Pre-Order Sale**: $30/box; pre-order by 11/4 (Wed), pick up on 11/8 (Sun).
     - **Catholic Biblical Apostolate in the Americas: 2026 Word Festival (Feast of Tabernacles)**: 11/6–11/8 via Zoom by Fr. Gabriel Seung-ui Hong.
     - **St. Joseph Society (Men's Ministry) Oktoberfest Thank You Message**: Gratitude to volunteers and parishioners for the 1st Oktoberfest on 10/25.
     - **All Souls' Day Memorial Mass**: 11/7 (Sat), Prayers for the Deceased at 1:40 PM, Memorial Mass at 2:00 PM at Gate of Heaven Catholic Cemetery Chapel (jointly with Oakland Korean Catholic Community; offerings accepted at the office from 11/1 or on-site).
     - **Wednesday Evening Mass Date Change**: Starting in November, moved from the first Wednesday to the last Wednesday of each month at 7:30 PM.
     - **Charity Committee Seeking Helping Hands**: Outreach request link for community members in need.
     - **Share Your Stories!**: Open invitation to share reflections, essays, or poems via email to Father.

5. **Updated Pope's Monthly Intention & Offertory**:
   - Month: `November`
   - Title: `For the proper use of wealth`
   - Text: `Let us pray for the proper use of wealth, that not succumbing to the temptation of selfishness, it may always be put at the service of the common good and solidarity of those who have less.`
   - Offertory: Mass Offertory ($1,344 Korean + $448 English), Annual Pledge ($5,440), Vocation Promotion ($320), Bishop's Appeal ($380), Total ($7,932).

6. **Automated Cross-Check**:
   - Validated static blocks and terminology consistency via `scripts/validate_bulletin.py` (0 errors).
   - Executed `scripts/check_facility_reservations.py docs/bulletins/2026-11-01.html` against `https://youngkjoo.github.io/ses-schedule/`. All 4 community events matched 100%!

7. **Generated Output & Published**:
   - Saved the Markdown draft to [weekly_translation_draft_2026-11-01.md](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/drafts/weekly_translation_draft_2026-11-01.md).
   - Generated the styled HTML page at [2026-11-01.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-11-01.html).
   - Updated navigation link on [2026-10-25.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-10-25.html) to link forward to November 1.
   - Updated main archive page [index.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/index.html) with November 1 and shifted `Latest` badge.
