# Weekly Bulletin Translation Job Walkthrough (October 25, 2026)

We have successfully executed the weekly bulletin translation and publishing job for **October 25, 2026**.

## Summary of Completed Work

1. **Retrieved the Latest Korean Bulletin**:
   - Fetched the latest bulletin post directly from `https://www.tvkcc.org/weeklybulletins/` (Post: `연중 제30주일 / 10-25-2026(제765호)`).
   - Downloaded the official PDF from `https://www.tvkcc.org/wp-content/uploads/2026/10/10252026_765.pdf`.

2. **Extracted Liturgical Info & Colors**:
   - Sunday Liturgical Title: **Thirtieth Sunday in Ordinary Time** (No. 765).
   - Liturgical Color Class: `liturgical-green` (RGB `[0.2196, 0.4627, 0.1137]`, Hex `#38761d`).

3. **Extracted Sunday School & Priest Schedule via Vision OCR & Extraction**:
   - Analyzed the Page 1 schedule table and prayer list:
     - 10/25: Sunday School Y, Priest: Fr. Augustine
     - 11/1: Sunday School Y, Priest: Fr. Gerald
     - 11/8: Sunday School Y, Priest: Fr. Paul
     - 11/15: Sunday School Y, Priest: Fr. Jim
   - Prayer list: `윤정의 알퐁소, 이순옥 데레사, 김정희 데레사, 정종락 필립보, 배정례 엘리사벳, 이데이빗 바오로, 이혁주 베드로, 이정수 비오, 권진주 마르가리타, 한규용 바오로, 한지아 클레어` (each wrapped in `<span>` tags with `&nbsp;` to prevent line break splits).

4. **Translated and Cataloged Announcements**:
   - Translated 10 announcements following the style guide and balanced two-column distribution:
     - **Education Committee**: RCIA class inquiry (Sunday 10:45 AM in CCOP Office) and rosary donations for catechumens by 11/1 (Sun).
     - **TVCS Bake Sale Event Notice**: 11/1 (Sun) after 9:30 AM and 11:00 AM Masses in the Church vestibule.
     - **Catholic Biblical Apostolate in the Americas: 2026 Word Festival (Feast of Tabernacles)**: 11/6–11/8 via Zoom by Fr. Gabriel Seung-ui Hong.
     - **Sunday School Events Notice**: Halloween Party today (10/25) at 9:30 AM in the Gym.
     - **St. Joseph Society Oktoberfest**: Today (10/25) from 10:30 AM to 3:00 PM in the church parking lot.
     - **St. Mary's Society Acorn Noodles Pre-Order Sale**: Pre-order after Korean Mass on 11/1 and 11/8; pick up on 11/15 ($15 / 3 lbs).
     - **Charity Committee Seeking Helping Hands**: Outreach request link for community members in need.
     - **All Souls' Day Memorial Mass**: 11/7 (Sat) 2:00 PM at Gate of Heaven Cemetery with Oakland Korean Catholic Community.
     - **Wednesday Evening Mass Date Change**: Starting in November, moved from the first Wednesday to the last Wednesday of each month at 7:30 PM.
     - **Share Your Stories!**: Monthly newsletter submissions invited via email or Google Docs.

5. **Updated Pope's Monthly Intention & Offertory**:
   - Month: `October`
   - Title: `For mental health ministry`
   - Text: `Let us pray that the mental health ministry be established throughout the Church, helping to overcome the stigma and discrimination of persons with mental illnesses.`
   - Offertory: Mass Offertory ($1,924 Korean + $403 English), Annual Pledge ($3,390), Vocation Promotion ($120), Bishop's Appeal ($125), Total ($5,562).

6. **Automated Cross-Check**:
   - Validated static blocks and terminology consistency via `scripts/validate_bulletin.py` (0 errors).
   - Executed `scripts/check_facility_reservations.py docs/bulletins/2026-10-25.html` against `https://youngkjoo.github.io/ses-schedule/`. Note: No `모임 안내` (Community Events) table was included in the 10/25 Korean bulletin, and key upcoming liturgical dates (e.g., 11/5 Daily Mass in Chapel, 11/14 Marian Devotion Mass in Chapel) were verified against the SES facility reservation schedule.

7. **Generated Output & Published**:
   - Saved the Markdown draft to [weekly_translation_draft_2026-10-25.md](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/drafts/weekly_translation_draft_2026-10-25.md).
   - Generated the styled HTML page at [2026-10-25.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-10-25.html).
   - Updated navigation link on [2026-10-18.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-10-18.html) to link forward to October 25.
   - Updated main archive page [index.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/index.html) with October 25 and shifted `Latest` badge.
