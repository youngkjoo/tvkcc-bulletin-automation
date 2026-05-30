# TVKCC English Bulletin Style Guide

Based on analysis of translated bulletins (2024–2026, 103+ PDFs), this style guide establishes the strict formatting rules for the English version of the TVKCC Weekly Announcements.

## 1. General Formatting & Typography
- **Religious Terms:** Use **Church** instead of Cathedral when referring to the local parish building. Use **Church vestibule** for locations. Use **Infant Baptism** instead of Baptism.
- **Personnel:** Use **Basic Christian Faith Community Lead** instead of Chief District Leader.
- **Bible Groups:** Format small groups as **Luke #8** instead of Luca 8.
- **Dates:** Always format dates as `M/D (Day)` (e.g., `4/26 (Sun)` or `5/3 (Sun)`). Use **Pre-order period** instead of Reservation for sales events.
- **Bullet Points:** Use standard markdown asterisks (`*`) for all bullets. Do NOT use Unicode characters like `●` or `◦`.
- **Header:** Every bulletin starts with the liturgy title and date on the same line, e.g., `Fifth Sunday of Easter  5/3/2026`

## 2. Liturgy Schedule
Format this as a simple bulleted list with the date, day, and event name.
**Important:** If a liturgy item has a sub-note (e.g., a donation deadline), include it as a sentence immediately after the item — not as a separate bullet.
**Example:**
* 5/3 (Sun) TVKCC Youth Day 9 AM mass, First communion, children's baptism, Youth Faith Festival
* 5/17 (Sun) Outdoor Mass & Marian Day (10 AM, combined Korean/English Mass), 11 AM CCOP Mass
  We are accepting donations for the outdoor mass by 5/10 (Sun). Submit your donation at the church office or to the pastoral council.

## 3. Community Events & Announcements
When translating announcements from the Korean bulletin, structure them with the main Title, followed by bulleted properties. Ensure consistency in property labels.
- **Combined properties:** When multiple short properties logically group together, you may combine them on a single line using `/` separators (e.g., `Hosted by: ... / Target: ...`).
- **Combined Date/time/location:** If concise, use `Date/time/location:` on a single line.
- Standard keys:
  - `* Hosted by:` / `* Target:`
  - `* Date/time:` or `* Date:` or `* Date/time/location:`
  - `* Location:`
  - `* Target:` or `* Who:`
  - `* Contact:`
  - `* Fee:`
  - `* Menu:`

**Example:**
**2026 Mother's Day Event**
* Hosted by: St. Joseph Society / Target: All parishioners
* Date/time/location: 5/10 (Sun), 10:45 AM - 12:45 PM, Gym
* Menu: Bossam, bindaetteok, buckwheat noodles, makgeolli, and special menu
* Fee: Free (Dine-in only, sorry we won't be able to provide to-go)
* Contact: 장진환 라파엘 (408) 722-7383

*Note: Maintain Korean names alongside their baptismal names (e.g., 유연호 안나).*

## 4. Offertory and Donations Table
Start with the payable-to note: `Please make checks payable to Tri-Valley Korean Catholic Church`

The financial data requires strict column adherence. List amounts in these exact categories:
1. **Mass Offertory (Korean)**
2. **Mass Offertory (English)**
3. **Annual Pledge** (교무금)
4. **Vocation Promotion** (성소후원)
5. **Bishop's Appeal**
6. **Total**

After the table, add the note: `The inquiry of the annual pledge is everyone's responsibility.`

Translate the lists of donors by grouping them under the English category names using standard markdown lists (which will translate to `<ul>` and `<li>` in HTML, specifically using `<ul class="donor-list">`):
* 교무금 (Inquiry of Annual Pledge)
* 성소후원 (Vocation Promotion)
* Bishop's Appeal
* 건축봉헌 (Church building fund)
* 감사 봉헌금 (**Thanksgiving**)

## 5. Sunday School & Priest Schedule Table
Format as a simple table with three columns: **Date**, **Sunday School (Y/N)**, and **Priest Name**.
**Example:**
| Date | Sunday School | Priest |
|------|--------------|--------|
| 5/3/2026 | N | Fr. Jim |
| 5/10/2026 | N | Fr. Gerald |

**Mass & Devotion Standard Labels:**
- **Confession**: Before weekday & Sunday masses<br>9 AM - 9:25 AM
- **Legion of Mary**: Before & after weekday and Sunday masses (Label: **Legion of Mary:** followed by <br>)
- **Holy Hour**: Monthly, after 1st Thursday mass (Label: **Holy Hour:** followed by <br>)
- **Ultreya**: 3rd Sunday after Mass (Label: **Ultreya:** followed by <br>)
- **Secular Franciscan**: 2nd Sunday 1:00 PM (Label: **Secular Franciscan:** followed by <br>)

## 6. We Ask For Your Prayer
When translating the prayer list, list the names in the standard format: `[Korean Name] [Baptismal Name]`, separated by commas.
End with: `Contact the office if there's someone in need of prayer`
**Example:** 윤정의 알퐁소, 박길순 수산나, 이순옥 데레사

## 7. Liturgical Colors
The background color of the header title bar row (with the liturgical week name and date) must change based on the liturgical calendar to match the original Korean PDF:
- **Red** (`.liturgical-red`): background `#e60000`, white title. Used for Pentecost Sunday, Palm Sunday, Good Friday, etc.
- **Green** (`.liturgical-green`): background `#2d662b`, gold title. Used for Ordinary Time.
- **Purple** (`.liturgical-purple`): background `#572478`, gold title. Used for Advent and Lent.
- **White/Gold** (`.liturgical-white`): background `#f4ddb4`, black title and black foreground. Used for Easter season, Christmas season, and specific solemnities/feasts.
- **Rose** (`.liturgical-rose`): background `#b55a82`, pink title. Used for Laetare and Gaudete Sundays.

## 8. Page Layout & Grid Balance
- **Expanded Page Width:** The overall page layout width is expanded to `1000px` (a 25% increase from the original 800px) to give sections ample breathing room.
- **Equal-Width Bottom Row:** Display the *Sunday School/Priest Schedule* table and the *Please pray for* box side-by-side in equal-width (50% / 50%) columns directly under the Mass Schedule.
- **Side-by-Side Offertory & Pope Intention:** The *Offertory and Donations* column and the *Pope's Monthly Intention & Giving* (Pope's Intention Box + Online Giving QR code) column are displayed side-by-side in a two-column grid matching the announcements above.

---
*Last updated: 2026-05-30 (Incorporated user edits on liturgical white color, layout expansion, and side-by-side grids)*

*This style guide ensures the translated output generated by the Antigravity Agent can be directly copy-pasted into the Google Doc template without breaking the established community standards.*
