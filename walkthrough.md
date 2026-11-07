# Weekly Bulletin Translation Job Walkthrough (November 8, 2026)

We have successfully executed the weekly bulletin translation and publishing job for **November 8, 2026**.

## Summary of Completed Work

1. **Retrieved the Latest Korean Bulletin**:
   - Fetched the latest bulletin post directly from `https://www.tvkcc.org/weeklybulletins/` (Post: `연중 제32주일(평신도 주일) / 11-8-2026(제767호)`).
   - Downloaded the official PDF from `https://www.tvkcc.org/wp-content/uploads/2026/11/11082026_767.pdf`.

2. **Extracted Liturgical Info & Colors**:
   - Sunday Liturgical Title: **Thirty-Second Sunday in Ordinary Time** (No. 767; parenthetical theme omitted per style guide).
   - Liturgical Color Class: `liturgical-green` (RGB `[0.2196, 0.4627, 0.1137]`, Hex `#38761d`).

3. **Extracted Sunday School & Priest Schedule via Vision OCR & Extraction**:
   - Analyzed the Page 1 schedule table and prayer list:
     - 11/8: Sunday School Y, Priest: Fr. Paul
     - 11/15: Sunday School Y, Priest: Fr. Paul
     - 11/22: Sunday School N, Priest: Fr. Paul
     - 11/29: Sunday School N, Priest: Fr. Paul
   - Prayer list: `윤정의 알퐁소, 이순옥 데레사, 김정희 데레사, 정종락 필립보, 배정례 엘리사벳, 이데이빗 바오로, 이정수 비오, 권진주 마르가리타, 한규용 바오로, 한지아 클레어` (10 names; `이혁주 베드로` removed this week; each wrapped in `<span>` tags with `&nbsp;` to prevent line break splits).

4. **Translated Community Events & Announcements**:
   - **Community Events (`모임 안내`)**:
     - Mother of Love Curia: 11/8 (Sun) 10:45 AM - 12:00 PM, Room A
     - Secular Franciscan Order: 11/8 (Sun) 1:00 PM, Room B
     - Matthew #4: 11/14 (Sat) 4:00 PM, Room A
     - Luke #3: 11/15 (Sun) 3:00 PM, 하성곤 요제프's home
     - Luke #1: 11/17 (Tue) 10:00 AM, Cry Room
     - Altar Servers (Advent Wreath Making): 11/28 (Sat) 6:00 PM - 8:00 PM, Gym
   - **Announcements (10 items, balanced across two columns)**:
     - **St. Mary's Society Acorn Noodles Pre-Order Pick-up**: Pick up today, 11/8 (Sun).
     - **St. Mary's Society 2nd Half General Assembly**: 11/22 (Sun) 10:45 AM – 11:15 AM in Room A.
     - **TVKCC Ultreya November Meeting**: 11/15 (Sun) 11:00 AM in Room A (discussing 2026 year-end gathering).
     - **Concern America Craft Sale**: 11/15 (Sun) before and after the Korean and English Masses.
     - **Education Committee**: RCIA class inquiry (Sunday 11:00 AM – 12:00 PM in CCOP Office) and rosary/prayer book donations.
     - **TVCS Thank You Message**: Raised $644 at last Sunday's Bake Sale for World Youth Day 2027.
     - **Catholic Biblical Apostolate in the Americas**: Tri-Valley Ministers of the Word Meeting (11/16 Mon 7:00 PM, Zoom) and Northern California Ministers of the Word Monthly Training (11/16 Mon 7:30 PM, Zoom, Lecturer: Fr. Maron Cheun Young-su).
     - **Advent Wreath Making Event Hosted by St. Mary's Society**: 11/28 (Sat) 5:00 PM – 8:00 PM in Room A ($40 participation / $40 pre-made purchase).
     - **Wednesday Evening Mass Date Change**: Starting in November, moved from the first Wednesday to the last Wednesday of each month at 7:30 PM.
     - **Charity Committee Seeking Helping Hands**: Outreach request link for community members in need.

5. **Updated Pope's Monthly Intention & Offertory**:
   - Month: `November`
   - Title: `For the proper use of wealth`
   - Text: `Let us pray for the proper use of wealth, that not succumbing to the temptation of selfishness, it may always be put at the service of the common good and solidarity of those who have less.`
   - Offertory: Mass Offertory ($1,955 Korean + $828 English), Annual Pledge ($5,220), Vocation Promotion ($250), Bishop's Appeal ($220), Total ($8,473).

6. **Automated Cross-Check**:
   - Validated static blocks and terminology consistency via `scripts/validate_bulletin.py` (0 errors).
   - Executed `scripts/check_facility_reservations.py docs/bulletins/2026-11-08.html` against `https://youngkjoo.github.io/ses-schedule/`.

7. **Generated Output & Published**:
   - Saved the Markdown draft to [weekly_translation_draft_2026-11-08.md](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/drafts/weekly_translation_draft_2026-11-08.md).
   - Generated the styled HTML page at [2026-11-08.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-11-08.html).
   - Updated navigation link on [2026-11-01.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-11-01.html) to link forward to November 8.
   - Updated main archive page [index.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/index.html) with November 8 and shifted `Latest` badge.
