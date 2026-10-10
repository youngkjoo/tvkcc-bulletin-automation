# Weekly Bulletin Translation Job Walkthrough (October 11, 2026)

We have successfully executed the weekly bulletin translation and publishing job for **October 11, 2026**.

## Summary of Completed Work

1. **Retrieved the Latest Korean Bulletin**:
   - Fetched the latest bulletin post directly from `https://www.tvkcc.org/weeklybulletins/` (Post: `연중 제28주일(군인 주일) / 10-11-2026(제763호)`).
   - Downloaded the official PDF from `https://www.tvkcc.org/wp-content/uploads/2026/10/10112026_763.pdf`.

2. **Extracted Liturgical Info & Colors**:
   - Sunday Liturgical Title: **Twenty-Eighth Sunday in Ordinary Time** (main liturgical name, omitted parenthetical annotation per style guide).
   - Liturgical Color Class: `liturgical-green` (RGB `[0.2196, 0.4627, 0.1137]`, Hex `#38761d`).

3. **Extracted Sunday School & Priest Schedule via Vision OCR & Extraction**:
   - Analyzed the Page 1 schedule table and prayer list:
     - 10/11: Sunday School Y, Priest: Fr. Paul
     - 10/18: Sunday School Y, Priest: Fr. Paul
     - 10/25: Sunday School Y, Priest: Fr. Augustine
     - 11/1: Sunday School Y, Priest: Fr. Gerald
   - Prayer list: `윤정의 알퐁소, 이순옥 데레사, 김정희 데레사, 정종락 필립보, 배정례 엘리사벳, 이데이빗 바오로, 이혁주 베드로, 이정수 비오, 권진주 마르가리타, 한규용 바오로, 한지아 클레어, 주종남 바오로` (each wrapped in `<span>` tags with `&nbsp;` to prevent line break splits).

4. **Translated and Cataloged Announcements**:
   - Translated 9 announcements following the style guide and balanced two-column distribution:
     - **Senatus Legion of Mary Congress**: 10/24 (Sat) at Cathedral of St. Mary of the Assumption, SF.
     - **Fundraising Sale for Reno Mission**: Gochujang, Doenjang, Cheonggukjang powder, honey, plum extract sale by St. Anne's Society.
     - **Catholic Bible Study Guide**: Young Adult "JJAL" Bible study (Zoom, 5 sessions) and Blessed Bible Reading (Senior Matthew, General Numbers via Zoom).
     - **29th Central West Regional Ultreya**: 10/17 (Sat) 9 AM – 5 PM at TVKCC.
     - **Sunday School Events Notice**: Confirmation & Pre-Confirmation 1st Retreat (10/23–25 at Redwood Glen) and Halloween Party (10/25 9:30 AM in Gym).
     - **St. Joseph Society Oktoberfest**: 10/25 (Sun) after 9:30 AM Mass in church parking lot.
     - **Charity Committee Seeking Helping Hands**: Outreach request link for community members in need.
     - **Diocese of Oakland Multicultural Festival (Chautauqua 2026)**: 10/17 (Sat) at The Cathedral of Christ the Light, Oakland.
     - **Congratulations on Diaconate Ordination**: Br. Young-kyun John Moon, S.J. on 10/23 (Fri) 6 PM at St. Leo the Great Church.

5. **Updated Pope's Monthly Intention & Offertory**:
   - Month: `October`
   - Title: `For mental health ministry`
   - Text: `Let us pray that the mental health ministry be established throughout the Church, helping to overcome the stigma and discrimination of persons with mental illnesses.`
   - Offertory: Mass Offertory ($1,833 Korean + $928 English), Annual Pledge ($4,265), Vocation Promotion ($190), Bishop's Appeal ($190), Total ($7,406).

6. **Automated Cross-Check**:
   - Executed `scripts/check_facility_reservations.py docs/bulletins/2026-10-11.html` against `https://youngkjoo.github.io/ses-schedule/`.
   - Identified a discrepancy for Matthew #1 & #2 on 10/16 (Bulletin lists "Online", SES facility schedule has Room A booked 7:30 PM - 9:30 PM).

7. **Generated Output & Published**:
   - Saved the Markdown draft to [weekly_translation_draft_2026-10-11.md](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/drafts/weekly_translation_draft_2026-10-11.md).
   - Generated the styled HTML page at [2026-10-11.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-10-11.html).
   - Updated navigation link on [2026-10-04.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-10-04.html) to link forward to October 11.
   - Updated main archive page [index.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/index.html) with October 11 and shifted `Latest` badge.
