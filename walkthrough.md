# Weekly Bulletin Translation Job Walkthrough (September 20, 2026)

We have successfully executed the weekly bulletin translation and publishing job for **September 20, 2026**.

## Summary of Completed Work

1. **Retrieved the Latest Korean Bulletin**:
   - Fetched the latest bulletin post directly from `https://www.tvkcc.org/weeklybulletins/` (Post: `한가위 / 9-20-2026(제760호)`).
   - Downloaded the official PDF from `https://www.tvkcc.org/wp-content/uploads/2026/09/09202026_760.pdf`.

2. **Extracted Liturgical Info & Colors**:
   - Sunday Liturgical Title: **Korean Thanksgiving Day (Chuseok)**
   - Liturgical Color Class: `liturgical-white` (White/Gold fill color `#f4ddb4`).

3. **Extracted Sunday School & Priest Schedule via Vision OCR**:
   - Analyzed the Page 1 schedule table and prayer list:
     - 9/20: Sunday School N, Priest: Fr. Paul
     - 9/27: Sunday School N, Priest: Bishop Simon (Bishop Simon Joo-young Kim)
     - 10/4: Sunday School Y, Priest: Fr. Gerald (tentative)
     - 10/11: Sunday School Y, Priest: Fr. Jim
   - Prayer list: `윤정의 알퐁소, 이순옥 데레사, 김정희 데레사, 정종락 필립보, 배정례 엘리사벳, 이데이빗 바오로, 이혁주 베드로, 이정수 비오, 권진주 마르가리타, 한규용 바오로, 한지아 클레어` (each wrapped in `<span>` tags with `&nbsp;` to prevent line break splits).

4. **Translated and Cataloged Announcements**:
   - Translated 12 announcements following the style guide and strict Korean PDF ordering:
     - **Sacrament of Confirmation Information**: 9/27 during 9:30 AM Mass, rehearsal 9/20 12 PM in Church, no confession before Mass, candidate interview before Mass.
     - **Bishop Simon Joo-young Kim Arrival & Departure Schedule**: Arrival 9/21 10:40 AM (SFO), Departure 9/28 12:50 PM (SFO).
     - **Invitation to Hike with the Bishop**: 9/23 (Wed) Lake Chabot, apply by today.
     - **Meeting with St. Anne's Society (성모회) & the Bishop**: 9/24 (Thu) 10:30 AM at Sports Park.
     - **Appointment**: RCIA Catechist 이복준 세실리아 (Cecilia Lee).
     - **Parishioners Lunch with the Bishop (Registration & Headcount)**: 9/27 1 PM at Bridges Clubhouse.
     - **2nd TVKCC Men's Choir Concert 'Our Voices'**: 10/3 (Sat) 5:30 PM – 7:00 PM in Church.
     - **Parish Facilities Notice**: Usage restrictions during Cursillo events (9/24–27).
     - **Charity Committee Seeking Helping Hands**: Community outreach link.
     - **Catholic Bible Study Group Recruitment**: Senior class, Acts, Genesis–Romans.
     - **WYD Participation Information Link**: Registration deadline 9/30.
     - **Novena Intentions for Confirmation Candidates**: Daily intentions from 9/20 to 9/26 + 24 candidates list.

5. **Updated Pope's Monthly Intention**:
   - Month: `September`
   - Title: `For the care of water`
   - Text: `Let us pray for a just and sustainable management of water, a vital resource so that everyone may have equal access to it.`

6. **Automated Cross-Check**:
   - Executed `scripts/check_facility_reservations.py docs/bulletins/2026-09-20.html` against `https://youngkjoo.github.io/ses-schedule/` — all 4 community events matched 100%!

7. **Generated Output & Published**:
   - Saved the Markdown draft to [weekly_translation_draft_2026-09-20.md](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/drafts/weekly_translation_draft_2026-09-20.md).
   - Generated the styled HTML page at [2026-09-20.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-09-20.html).
   - Updated navigation link on [2026-09-13.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-09-13.html) to link forward to September 20.
   - Updated main archive page [index.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/index.html) (shifted `Latest` badge to September 20).
