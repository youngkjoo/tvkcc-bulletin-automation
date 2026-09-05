#!/usr/bin/env python3
import sys
import os
import re
import json
import urllib.request
import bs4

def get_calendar_data():
    url = "https://youngkjoo.github.io/ses-schedule/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        match = re.search(r'const calendarData = (\[[\s\S]*?\]);\s*let activeMonthKey', html)
        if match:
            return json.loads(match.group(1))
    except Exception as e:
        print(f"Error fetching calendar data: {e}", file=sys.stderr)
    return None

def check_reservations(html_path):
    if not os.path.exists(html_path):
        print(f"File not found: {html_path}", file=sys.stderr)
        return

    with open(html_path, 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f.read(), 'html.parser')

    # Extract bulletin date from title or filename (e.g. 2026-09-06)
    filename = os.path.basename(html_path)
    date_match = re.match(r'(\d{4})-(\d{2})-(\d{2})', filename)
    if not date_match:
        print("Could not parse date from filename.", file=sys.stderr)
        return

    year, month_str, _ = date_match.groups()
    month_int = int(month_str)

    calendar_data = get_calendar_data()
    if not calendar_data:
        print("Failed to load SES calendar data.")
        return

    # Extract events from events-table if present
    events = []
    events_table = soup.select_one(".events-table")
    if events_table:
        for row in events_table.select("tbody tr"):
            cols = [c.get_text(strip=True) for c in row.find_all("td")]
            if len(cols) == 3:
                event_name, date_time, location = cols
                events.append({
                    "event": event_name,
                    "date_time": date_time,
                    "location": location
                })

    if not events:
        print("No Community Events table found in bulletin.")
        return

    print("### Community Events Cross-Check (SES Facility Reservation Schedule)\n")
    print("| Event / Group | Bulletin Listing | SES Schedule Entry | Status / Difference |")
    print("| :--- | :--- | :--- | :--- |")

    for ev in events:
        ev_name = ev["event"]
        dt = ev["date_time"]
        loc = ev["location"]

        # Parse date from date_time (e.g., '9/6 (Sun) 11:00 AM' or '9/13 (Sun) 10:45 AM - 12:00 PM')
        m_match = re.search(r'(\d{1,2})/(\d{1,2})', dt)
        if not m_match:
            print(f"| **{ev_name}** | {dt}<br>{loc} | Unknown Date Format | ❓ Manual check needed |")
            continue

        ev_month = int(m_match.group(1))
        ev_day = int(m_match.group(2))

        # Find month in calendar
        month_key = f"{year}-{ev_month}"
        month_obj = next((m for m in calendar_data if m.get("key") == month_key), None)

        if not month_obj:
            print(f"| **{ev_name}** | {dt}<br>{loc} | Month {month_key} not in schedule | ❌ Not Found |")
            continue

        day_obj = next((d for d in month_obj.get("days", []) if d.get("day") == ev_day), None)
        if not day_obj:
            print(f"| **{ev_name}** | {dt}<br>{loc} | Day {ev_day} not in schedule | ❌ Not Found |")
            continue

        # Look across room bookings for matching group / event
        matched_bookings = []
        all_day_bookings = []
        for room, blist in day_obj.get("bookings", {}).items():
            for b in blist:
                b_entry = {**b, "room": room}
                all_day_bookings.append(b_entry)
                
                # Check for match by group or event name keywords
                keywords = re.split(r'[\s/#,-]+', ev_name.lower())
                keywords = [k for k in keywords if len(k) > 1 and k not in ['the', 'of', 'and', 'meeting', 'group', 'room']]
                
                b_str = f"{b.get('group', '')} {b.get('event', '')}".lower()
                
                # Special aliases
                if "curia" in ev_name.lower() and "curia" in b_str:
                    matched_bookings.append(b_entry)
                elif "franciscan" in ev_name.lower() and "franciscan" in b_str:
                    matched_bookings.append(b_entry)
                elif "altar" in ev_name.lower() and "altar" in b_str:
                    matched_bookings.append(b_entry)
                elif "leader" in ev_name.lower() and ("leader" in b_str or "faith community" in b_str):
                    matched_bookings.append(b_entry)
                elif any(k in b_str for k in keywords if len(k) >= 3):
                    matched_bookings.append(b_entry)

        if matched_bookings:
            # Check room match
            room_matched = any(b["room"].lower() in loc.lower() or loc.lower() in b["room"].lower() for b in matched_bookings)
            
            entry_strs = [f"`[{b['room']}]` {b.get('time', '')} {b.get('event', '')} ({b.get('group', '')})" for b in matched_bookings]
            entry_display = "<br>".join(entry_strs)
            
            if room_matched:
                status = "✅ **Exact Match**"
            else:
                rooms_in_sched = ", ".join(set(b['room'] for b in matched_bookings))
                status = f"⚠️ **Room Mismatch**<br>*(Bulletin: {loc}; Schedule: {rooms_in_sched})*"
            
            print(f"| **{ev_name}** | **{dt}**<br>{loc} | {entry_display} | {status} |")
        else:
            print(f"| **{ev_name}** | **{dt}**<br>{loc} | No specific booking found on {ev_month}/{ev_day} | ⚠️ **Check Manually** |")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/check_facility_reservations.py docs/bulletins/YYYY-MM-DD.html")
        sys.exit(1)
    check_reservations(sys.argv[1])
