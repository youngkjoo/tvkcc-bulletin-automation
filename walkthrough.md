# Weekly Bulletin Translation Job Walkthrough (November 15, 2026)

We have successfully executed the weekly bulletin translation and publishing job for **November 15, 2026**.

## Summary of Completed Work

1. **Retrieved the Latest Korean Bulletin**:
   - Fetched the latest bulletin post directly from `https://www.tvkcc.org/weeklybulletins/` (Post: `연중 제33주일(세계 가난한 이의 날) / 11-15-2026(제768호)`).
   - Downloaded the official PDF from `https://www.tvkcc.org/wp-content/uploads/2026/11/11152026_768.pdf`.

2. **Extracted Liturgical Info & Colors**:
   - Sunday Liturgical Title: **Thirty-Third Sunday in Ordinary Time** (No. 768; parenthetical theme omitted per style guide).
   - Liturgical Color Class: `liturgical-green` (RGB `[0.2196, 0.4627, 0.1137]`, Hex `#38761d`).

3. **Extracted Sunday School & Priest Schedule via Vision OCR & Extraction**:
   - Analyzed the Page 1 schedule table and prayer list:
     - 11/15: Sunday School Y, Priest: Fr. Paul
     - 11/22: Sunday School N, Priest: Fr. Paul
     - 11/29: Sunday School N, Priest: Fr. Paul
     - 12/6: Sunday School Y, Priest: Fr. Gerald
   - Prayer list: `윤정의 알퐁소, 이순옥 데레사, 김정희 데레사, 정종락 필립보, 배정례 엘리사벳, 이데이빗 바오로, 이정수 비오, 권진주 마르가리타, 한규용 바오로, 한지아 클레어` (10 names; each wrapped in `<span>` tags with `&nbsp;` to prevent line break splits).

4. **Translated Community Events & Announcements**:
   - **Community Events (`모임 안내`)**:
     - Luke #3: 11/15 (Sun) 3:00 PM, 하성곤 요제프's home
     - Luke #1: 11/17 (Tue) 10:00 AM, Cry Room
     - Matthew #1 & #2: 11/20 (Fri) 7:30 PM, Room A
     - St. Joseph Society (Men's Ministry) Monthly Meeting: 11/21 (Sat) 6:00 PM, Gym
     - Altar Servers (Advent Wreath Making): 11/28 (Sat) 6:00 PM - 8:00 PM, Gym
   - **Announcements (12 items, balanced 6 and 6 across two columns)**:
     - **TVKCC Ultreya November Meeting**: Today, 11/15 (Sun) 11:00 AM in Room A.
     - **Concern America Craft Sale**: Today, 11/15 (Sun) before and after the Korean and English Masses.
     - **Catholic Biblical Apostolate in the Americas**: Tri-Valley Ministers of the Word Meeting (11/16 Mon 7:00 PM, Zoom) and Northern California Ministers of the Word Monthly Training (11/16 Mon 7:30 PM, Zoom, Lecturer: Fr. Maron Cheun Young-su).
     - **St. Mary's Society 2nd Half General Assembly**: 11/22 (Sun) 10:45 AM – 11:15 AM in Room A.
     - **St. Mary's Society 4th Quarter Group Purchase**: Sesame oil, grains, and other agricultural/marine products; order deadline 11/23, pick-up 12/8 (Tue) before/after Mass.
     - **Advent Wreath Making Event Hosted by St. Mary's Society**: 11/28 (Sat) 5:00 PM – 8:00 PM in Room A ($40 participation / $40 pre-made purchase).
     - **Joachim and Anna Society 2026 Year-End Gathering**: 11/29 (Sun) 11:00 AM – 2:30 PM at The Bridges Club House in San Ramon.
     - **Education Committee**: RCIA class inquiry (Sunday 11:00 AM – 12:00 PM in CCOP Office) and rosary/prayer book donations.
     - **Bible Purchase Information**: Three sample Bible sizes available for inspection at the office desk in front of the Chapel before/after Mass for bulk ordering from Korea.
     - **2027 Daughters of St. Paul Bible School Accepting New Students**: Mail and online courses (Introductory 2 yrs, Intermediate 4 yrs, St. Paul Theology & Spirituality 1 yr) via `uus.pauline.or.kr`.
     - **Immanuel Festival · Share the Joy of Christmas Together**: 12/24 (Thu) after the 8:00 PM Mass in the Church; sign up by 11/29 (Sun) (first 5 teams; also recruiting 1–2 teams for after the 12/25 9:00 AM Mass).
     - **Charity Committee Seeking Helping Hands**: Outreach request link for community members in need.

5. **Updated Pope's Monthly Intention & Offertory**:
   - Month: `November`
   - Title: `For the proper use of wealth`
   - Text: `Let us pray for the proper use of wealth, that not succumbing to the temptation of selfishness, it may always be put at the service of the common good and solidarity of those who have less.`
   - Offertory: Mass Offertory ($1,780 Korean + $468 English), Annual Pledge ($2,560), Vocation Promotion ($170), Bishop's Appeal ($140), Total ($5,118).

6. **Automated Cross-Check**:
   - Validated static blocks and terminology consistency via `scripts/validate_bulletin.py` (0 errors).
   - Executed `scripts/check_facility_reservations.py docs/bulletins/2026-11-15.html` against `https://youngkjoo.github.io/ses-schedule/`.

7. **Generated Output & Published**:
   - Saved the Markdown draft to [weekly_translation_draft_2026-11-15.md](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/drafts/weekly_translation_draft_2026-11-15.md).
   - Generated the styled HTML page at [2026-11-15.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-11-15.html).
   - Updated navigation link on [2026-11-08.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-11-08.html) to link forward to November 15.
   - Updated main archive page [index.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/index.html) with November 15 and shifted `Latest` badge.
