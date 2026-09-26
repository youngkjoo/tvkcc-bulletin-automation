# Weekly Bulletin Translation Job Walkthrough (September 27, 2026)

We have successfully executed the weekly bulletin translation and publishing job for **September 27, 2026**.

## Summary of Completed Work

1. **Retrieved the Latest Korean Bulletin**:
   - Fetched the latest bulletin post directly from `https://www.tvkcc.org/weeklybulletins/` (Post: `연중 제26주일 / 9-27-2026(제761호)`).
   - Downloaded the official PDF from `https://www.tvkcc.org/wp-content/uploads/2026/09/09272026_761.pdf`.

2. **Extracted Liturgical Info & Colors**:
   - Sunday Liturgical Title: **Twenty-Sixth Sunday in Ordinary Time** (main liturgical name, omitted parenthetical theme per style guide).
   - Liturgical Color Class: `liturgical-green` (Green fill `#38761d` / RGB `(0.2196, 0.4627, 0.1137)`).

3. **Extracted Sunday School & Priest Schedule via Vision OCR & Extraction**:
   - Analyzed the Page 1 schedule table and prayer list:
     - 9/27: Sunday School N, Priest: Fr. Simon (Bishop Simon Joo-young Kim)
     - 10/4: Sunday School Y, Priest: Fr. Gerald (tentative)
     - 10/11: Sunday School Y, Priest: Fr. Jim
     - 10/18: Sunday School Y, Priest: Fr. Paul
   - Prayer list: `윤정의 알퐁소, 이순옥 데레사, 김정희 데레사, 정종락 필립보, 배정례 엘리사벳, 이데이빗 바오로, 이혁주 베드로, 이정수 비오, 권진주 마르가리타, 한규용 바오로, 한지아 클레어` (each wrapped in `<span>` tags with `&nbsp;` to prevent line break splits).

4. **Translated and Cataloged Announcements**:
   - Translated 9 announcements following the style guide and balanced two-column distribution:
     - **Congratulations on Receiving the Sacrament of Confirmation!**: Message to the 24 candidates and list of newly confirmed parishioners.
     - **Parishioners Lunch with the Bishop**: Today (9/27) 1:00 PM at Bridges Clubhouse.
     - **Thank You to Bishop Simon Joo-young Kim and Our Community**: Appreciation for bishop's pastoral visit.
     - **Bishop Simon Joo-young Kim Departure Schedule**: 9/28 (Mon) 12:50 PM at SFO.
     - **WYD Participation Information Link**: Registration link and deadline (9/30).
     - **2nd TVKCC Men's Choir Concert 'Our Voices'**: 10/3 (Sat) 5:30 PM in Church.
     - **Parish Facilities Notice**: Usage restrictions for Chapel & Adoration Room during Cursillo closing on 9/27.
     - **Charity Committee Seeking Helping Hands**: Volunteer registration link for community outreach.
     - **Catholic Bible Study Group Recruitment**: Word Sharing, Senior Matthew, and Numbers (Zoom).

5. **Updated Pope's Monthly Intention & Offertory**:
   - Month: `September`
   - Title: `For the care of water`
   - Text: `Let us pray for a just and sustainable management of water, a vital resource so that everyone may have equal access to it.`
   - Offertory: Mass Offertory ($2,040 Korean + $740 English), Annual Pledge ($1,750), Bishop's Appeal ($200), Total ($4,730).

6. **Automated Cross-Check**:
   - Executed `scripts/check_facility_reservations.py docs/bulletins/2026-09-27.html` against `https://youngkjoo.github.io/ses-schedule/`.

7. **Generated Output & Published**:
   - Saved the Markdown draft to [weekly_translation_draft_2026-09-27.md](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/drafts/weekly_translation_draft_2026-09-27.md).
   - Generated the styled HTML page at [2026-09-27.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-09-27.html).
   - Updated navigation link on [2026-09-20.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-09-20.html) to link forward to September 27.
   - Updated main archive page [index.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/index.html) (shifted `Latest` badge to September 27).
