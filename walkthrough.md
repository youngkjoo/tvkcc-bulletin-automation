# Weekly Bulletin Translation Job Walkthrough (October 4, 2026)

We have successfully executed the weekly bulletin translation and publishing job for **October 4, 2026**.

## Summary of Completed Work

1. **Retrieved the Latest Korean Bulletin**:
   - Fetched the latest bulletin post directly from `https://www.tvkcc.org/weeklybulletins/` (Post: `연중 제27주일 / 10-4-2026(제762호)`).
   - Downloaded the official PDF from `https://www.tvkcc.org/wp-content/uploads/2026/10/10042026_762.pdf`.

2. **Extracted Liturgical Info & Colors**:
   - Sunday Liturgical Title: **Twenty-Seventh Sunday in Ordinary Time**
   - Liturgical Color Class: `liturgical-green` (RGB `[0.2196, 0.4627, 0.1137]`, Hex `#38761d`).

3. **Extracted Sunday School & Priest Schedule via Vision OCR & Extraction**:
   - Analyzed the Page 1 schedule table and prayer list:
     - 10/4: Sunday School Y, Priest: Fr. Gerald
     - 10/11: Sunday School Y, Priest: Fr. Jim
     - 10/18: Sunday School Y, Priest: Fr. Paul
     - 10/25: Sunday School Y, Priest: Fr. Augustine
   - Prayer list: `윤정의 알퐁소, 이순옥 데레사, 김정희 데레사, 정종락 필립보, 배정례 엘리사벳, 이데이빗 바오로, 이혁주 베드로, 이정수 비오, 권진주 마르가리타, 한규용 바오로, 한지아 클레어, 주종남 바오로` (each wrapped in `<span>` tags with `&nbsp;` to prevent line break splits).

4. **Translated and Cataloged Announcements**:
   - Translated 7 announcements following the style guide and balanced two-column distribution:
     - **Fundraising Sale for Reno Mission**: Gochujang, Doenjang, Cheonggukjang powder, honey, plum extract sale by St. Anne's Society.
     - **Parish Open KakaoTalk Chatroom**: QR code guidance to join parish Open Chat for community news.
     - **Catholic Bible Study Guide**: Young Adult "JJAL" Bible study (Zoom, 5 sessions) and Blessed Bible Reading (Senior Matthew, General Numbers via Zoom).
     - **29th Central West Regional Ultreya**: 10/17 (Sat) 9 AM – 5 PM at TVKCC.
     - **Sunday School Events Notice**: Confirmation & Pre-Confirmation 1st Retreat (10/23–25 at Redwood Glen) and Halloween Party (10/25 9:30 AM in Gym).
     - **Charity Committee Seeking Helping Hands**: Outreach request link for community members in need.
     - **Diocese of Oakland Multicultural Festival (Chautauqua 2026)**: 10/17 (Sat) at The Cathedral of Christ the Light, Oakland.

5. **Updated Pope's Monthly Intention & Offertory**:
   - Month: `October`
   - Title: `For mental health ministry`
   - Text: `Let us pray that the mental health ministry be established throughout the Church, helping to overcome the stigma and discrimination of persons with mental illnesses.`
   - Offertory: Mass Offertory ($2,368 Korean + English —), Annual Pledge ($1,375.57), Vocation Promotion ($40), Bishop's Appeal ($40), Total ($3,823.57).

6. **Automated Cross-Check**:
   - Executed `scripts/check_facility_reservations.py docs/bulletins/2026-10-04.html` against `https://youngkjoo.github.io/ses-schedule/`. All on-site parish events matched SES room bookings.

7. **Generated Output & Published**:
   - Saved the Markdown draft to [weekly_translation_draft_2026-10-04.md](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/drafts/weekly_translation_draft_2026-10-04.md).
   - Generated the styled HTML page at [2026-10-04.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-10-04.html).
   - Updated navigation link on [2026-09-27.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-09-27.html) to link forward to October 4.
   - Updated main archive page [index.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/index.html) with a new October 2026 section and `Latest` badge.
