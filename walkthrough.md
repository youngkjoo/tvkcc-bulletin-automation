# Weekly Bulletin Translation Job Walkthrough (November 22, 2026)

We have successfully executed the weekly bulletin translation and publishing job for **November 22, 2026**.

## Summary of Completed Work

1. **Retrieved the Latest Korean Bulletin**:
   - Retrieved the bulletin post `https://www.tvkcc.org/6583-2/` (Title: `연중 제34주일(그리스도 왕 대축일) / 11-22-2026(제769호)`).
   - Downloaded the official PDF from `https://www.tvkcc.org/wp-content/uploads/2026/11/11222026-769.pdf` to `2026-11-22.pdf`.

2. **Extracted Liturgical Info & Colors**:
   - Sunday Liturgical Title: **Solemnity of Our Lord Jesus Christ, King of the Universe** (No. 769; parenthetical `(성서 주간)` omitted per style guide).
   - Liturgical Color Class: `liturgical-white` (RGB `(0.9569, 0.8667, 0.7059)`, Hex `#f4ddb4`).

3. **Extracted Sunday School & Priest Schedule via OCR & Extraction**:
   - Analyzed the Page 1 schedule table and prayer list:
     - 11/22: Sunday School N, Priest: Fr. Paul
     - 11/29: Sunday School N, Priest: Fr. Paul
     - 12/6: Sunday School Y, Priest: Fr. Gerald
     - 12/13: Sunday School Y, Priest: Fr. Jim
   - Prayer list: `윤정의 알퐁소, 이순옥 데레사, 김정희 데레사, 정종락 필립보, 배정례 엘리사벳, 이데이빗 바오로, 이정수 비오, 권진주 마르가리타, 한규용 바오로, 한지아 클레어` (10 names; each wrapped in `<span>` tags with `&nbsp;` to prevent line break splits).

4. **Translated Community Events & Announcements**:
   - **Community Events (`모임 안내`)**:
     - Altar Servers (Advent Wreath Making): 11/28 (Sat) 6:00 PM - 8:00 PM, Gym
     - Matthew #3: 12/5 (Sat) 4:30 PM, Room A
   - **Announcements (12 items, balanced 6 and 6 across two columns)**:
     - **St. Mary's Society 2nd Half General Assembly**: Today, 11/22 (Sun) 10:45 AM – 11:15 AM in Room A.
     - **Advent Wreath Making Event Hosted by St. Mary's Society**: 11/28 (Sat) 5:00 PM – 8:00 PM in Room A ($40 participation / $40 pre-made purchase).
     - **Concern America Craft Sale Thank You Note**: Thanking parishioners; $1,320 in sales proceeds will support low-income families in El Salvador, Guatemala, Mexico, and Bangladesh (Charity Committee).
     - **Confirmation Reunion**: 11/22 (Sun) or 11/29 (Sun) at 12:15 PM in Church (attend one date; faith sharing and guide to daily Bible reading).
     - **Education Committee**: RCIA class inquiry (Sunday 11:00 AM – 12:00 PM in CCOP Office) and rosary/prayer book donations.
     - **St. Mary's Society 4th Quarter Group Purchase**: Sesame oil, grains, and other agricultural/marine products; order deadline 11/23, pick-up 12/8 (Tue) before/after Mass.
     - **Joachim and Anna Society 2026 Year-End Gathering**: 11/29 (Sun) 11:00 AM – 2:30 PM at The Bridges Club House in San Ramon.
     - **2027 Daughters of St. Paul Bible School Accepting New Students**: Mail and online courses (Introductory 2 yrs, Intermediate 4 yrs, St. Paul Theology & Spirituality 1 yr) via `uus.pauline.or.kr`.
     - **2027 Catholic Catechetical Institute Correspondence Theology Course Accepting New Students**: 6-year correspondence program studying Scripture, Liturgy, and Church History via `http://ci.catholic.or.kr`.
     - **Immanuel Festival · Share the Joy of Christmas Together**: 12/24 (Thu) after the 8:00 PM Mass in the Church; sign up by 11/29 (Sun) (first 5 teams; also recruiting 1–2 teams for after the 12/25 9:00 AM Mass).
     - **Annual Giving Tree Event**: Hosted by CCOP and run by TVCS volunteer group, 11/22 (Sun) – 12/6 (Sun) at the Giving Tree table in the Church vestibule.
     - **Charity Committee Seeking Helping Hands**: Outreach request link for community members in need.

5. **Updated Pope's Monthly Intention & Offertory**:
   - Month: `November`
   - Title: `For the proper use of wealth`
   - Text: `Let us pray for the proper use of wealth, that not succumbing to the temptation of selfishness, it may always be put at the service of the common good and solidarity of those who have less.`
   - Offertory: Mass Offertory ($2,192 Korean + $499 English), Annual Pledge ($5,070), Vocation Promotion ($170), Bishop's Appeal ($170), Total ($8,101).

6. **Automated Cross-Check**:
   - Validated static blocks and terminology consistency via `scripts/validate_bulletin.py` (0 static block errors, 0 translation inconsistencies).
   - Executed `scripts/check_facility_reservations.py` against `https://youngkjoo.github.io/ses-schedule/`.

7. **Generated Output & Published**:
   - Saved the Markdown draft to [weekly_translation_draft_2026-11-22.md](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/drafts/weekly_translation_draft_2026-11-22.md).
   - Generated the styled HTML page at [2026-11-22.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-11-22.html).
   - Updated navigation link on [2026-11-15.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-11-15.html) to link forward to November 22.
   - Updated main archive page [index.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/index.html) with November 22 and shifted `Latest` badge.
