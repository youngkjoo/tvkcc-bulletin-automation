# Weekly Bulletin Translation Job Walkthrough (October 18, 2026)

We have successfully executed the weekly bulletin translation and publishing job for **October 18, 2026**.

## Summary of Completed Work

1. **Retrieved the Latest Korean Bulletin**:
   - Fetched the latest bulletin post directly from `https://www.tvkcc.org/weeklybulletins/` (Post: `민족들의 복음화를 위한 미사(전교 주일) / 10-18-2026(제764호)`).
   - Downloaded the official PDF from `https://www.tvkcc.org/wp-content/uploads/2026/10/10182026_764.pdf`.

2. **Extracted Liturgical Info & Colors**:
   - Sunday Liturgical Title: **Mass for the Evangelization of Peoples** (main liturgical name, omitted parenthetical annotation per style guide).
   - Liturgical Color Class: `liturgical-green` (RGB `[0.2196, 0.4627, 0.1137]`, Hex `#38761d`).

3. **Extracted Sunday School & Priest Schedule via Vision OCR & Extraction**:
   - Analyzed the Page 1 schedule table and prayer list:
     - 10/18: Sunday School Y, Priest: Fr. Paul
     - 10/25: Sunday School Y, Priest: Fr. Augustine
     - 11/1: Sunday School Y, Priest: Fr. Gerald
     - 11/8: Sunday School Y, Priest: Fr. Paul
   - Prayer list: `윤정의 알퐁소, 이순옥 데레사, 김정희 데레사, 정종락 필립보, 배정례 엘리사벳, 이데이빗 바오로, 이혁주 베드로, 이정수 비오, 권진주 마르가리타, 한규용 바오로, 한지아 클레어` (each wrapped in `<span>` tags with `&nbsp;` to prevent line break splits).

4. **Translated and Cataloged Announcements**:
   - Translated 9 announcements following the style guide and balanced two-column distribution:
     - **Senatus Legion of Mary Congress**: 10/24 (Sat) at Cathedral of St. Mary of the Assumption, SF.
     - **Fundraising Sale for Reno Mission**: Item pick-up and distribution today (10/18).
     - **Catholic Biblical Apostolate in the Americas: 2026 Word Festival (Feast of Tabernacles)**: 11/6–11/8 via Zoom by Fr. Gabriel Seung-ui Hong.
     - **Sunday School Events Notice**: Confirmation & Pre-Confirmation 1st Retreat (10/23–25 at Redwood Glen) and Halloween Party (10/25 9:30 AM in Gym).
     - **St. Joseph Society Oktoberfest**: 10/25 (Sun) 10:30 AM – 3:00 PM in church parking lot.
     - **Charity Committee Seeking Helping Hands**: Outreach request link for community members in need.
     - **Congratulations on Diaconate Ordination**: Br. Young-kyun John Moon, S.J. on 10/23 (Fri) 6 PM at St. Leo the Great Church.
     - **All Souls' Day Memorial Mass**: 11/7 (Sat) 2:00 PM at Gate of Heaven Cemetery with Oakland Korean Catholic Community.
     - **Wednesday Evening Mass Date Change**: Starting in November, moved from first Wednesday to last Wednesday of each month at 7:30 PM.

5. **Updated Pope's Monthly Intention & Offertory**:
   - Month: `October`
   - Title: `For mental health ministry`
   - Text: `Let us pray that the mental health ministry be established throughout the Church, helping to overcome the stigma and discrimination of persons with mental illnesses.`
   - Offertory: Mass Offertory ($1,787 Korean + $332 English), Annual Pledge ($4,045), Vocation Promotion ($300), Bishop's Appeal ($290), Total ($6,754).

6. **Automated Cross-Check**:
   - Executed `scripts/check_facility_reservations.py docs/bulletins/2026-10-18.html` against `https://youngkjoo.github.io/ses-schedule/`. All community events (Luke #1 on 10/20 in Cry Room, Matthew #5 on 10/24 in Room A) matched 100%!

7. **Generated Output & Published**:
   - Saved the Markdown draft to [weekly_translation_draft_2026-10-18.md](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/drafts/weekly_translation_draft_2026-10-18.md).
   - Generated the styled HTML page at [2026-10-18.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-10-18.html).
   - Updated navigation link on [2026-10-11.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-10-11.html) to link forward to October 18.
   - Updated main archive page [index.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/index.html) with October 18 and shifted `Latest` badge.
