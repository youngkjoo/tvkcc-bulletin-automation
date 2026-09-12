# Weekly Bulletin Translation Job Walkthrough (September 13, 2026)

We have successfully executed the weekly bulletin translation and publishing job for **September 13, 2026**.

## Summary of Completed Work

1. **Retrieved the Latest Korean Bulletin**:
   - Fetched the latest bulletin post directly from `https://www.tvkcc.org/weeklybulletins/` (Post: `연중 제24주일 / 9-13-2026(제759호)`).
   - Downloaded the official PDF from `https://www.tvkcc.org/wp-content/uploads/2026/09/09132026_759.pdf`.

2. **Extracted Liturgical Info & Colors**:
   - Sunday Liturgical Title: **Twenty-Fourth Sunday in Ordinary Time**
   - Liturgical Color Class: `liturgical-green` (Ordinary Time green).

3. **Extracted Sunday School & Priest Schedule via Vision OCR**:
   - Analyzed the Page 1 schedule table and prayer list:
     - 9/13: Sunday School N, Priest: Fr. Jim
     - 9/20: Sunday School N, Priest: Fr. Paul
     - 9/27: Sunday School N, Priest: Bishop Simon (Bishop Simon Joo-young Kim)
     - 10/4: Sunday School Y, Priest: Fr. Gerald (tentative)
   - Prayer list: `윤정의 알퐁소, 이순옥 데레사, 김정희 데레사, 정종락 필립보, 배정례 엘리사벳, 이데이빗 바오로, 이혁주 베드로, 이정수 비오, 권진주 마르가리타, 한규용 바오로, 한지아 클레어` (each wrapped in `<span>` tags with `&nbsp;` to prevent line break splits).

4. **Translated and Cataloged Announcements**:
   - Translated 10 announcements following the style guide and strict Korean PDF ordering:
     - **20th Anniversary of Pastor's Priesthood Ordination (Ordained on 2006.09.14)**
     - **Chuseok Joint Memorial Mass & Mass Intentions Offering** (9/20 Sun 9:00 AM combined Mass, deadline 9/15, office desk in front of Chapel; notice: *"There will be no general intentions on that day."*)
     - **Sacrament of Confirmation Information** (9/27 Sun during 9:30 AM Mass, rehearsal 9/20 after 11 AM Mass in Church with godparents)
     - **TVKCC Ultreya September Meeting** (9/20 Sun 11:00 AM, Room A)
     - **Novena Intentions for Confirmation Candidates** (9/18–9/26 daily intentions + candidate list)
     - **Charity Committee Seeking Helping Hands**
     - **Catholic Bible Study Group Recruitment**
     - **WYD Participation Information Link** (Deadline: 9/30)
     - **Parish Facilities Notice** (Usage restrictions during Cursillo events on 9/24–27)
     - **Funeral Mass for the Late Pyo Jae-deok Antonio** (9/17 Thu 10:30 AM Church, Viewing 10 AM Chapel, Burial 1 PM Holy Sepulchre, Reception 2 PM Ban Suk Jung)

5. **Updated Pope's Monthly Intention**:
   - Month: `September`
   - Title: `For the care of water`
   - Text: `Let us pray for a just and sustainable management of water, a vital resource so that everyone may have equal access to it.`

6. **Automated Cross-Check**:
   - Executed `scripts/check_facility_reservations.py docs/bulletins/2026-09-13.html` against `https://youngkjoo.github.io/ses-schedule/` — all 8 community events matched 100%!

7. **Generated Output & Published**:
   - Saved the Markdown draft to [weekly_translation_draft_2026-09-13.md](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/drafts/weekly_translation_draft_2026-09-13.md).
   - Generated the styled HTML page at [2026-09-13.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-09-13.html).
   - Updated navigation link on [2026-09-06.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/bulletins/2026-09-06.html) to link forward to September 13.
   - Updated main archive page [index.html](file:///Users/youngjoo/Vibe/TVKCC%20Jubo/docs/index.html) (shifted `Latest` badge to September 13).
   - Cleaned up all temporary files inside `temp_extraction/`.
