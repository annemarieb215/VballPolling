from datetime import date

DROP_INS = []
COURTS = {"16": "1 court", "32": "2 courts", "48": "3 courts"}
ADV_DROPIN_DAYS = {"Saturday", "Sunday"}
INT_DROPIN_DAYS = {"Wednesday"}
LVL3_DAYS = {"Monday", "Wednesday","Saturday"}
LVL4_DAYS = {"Thursday"}
LVL2_3_DAYS = {"Friday"}
WOMENS_DAYS = {"Saturday"}
SUNDAY_SKILLS = {"Sunday"}

def parse(events, weekday):
    #parse through web events
    for event in events:
        title = (event.find("h6", class_="flex-grow-1 text-truncate mb-0 mr-2")).text.strip()
        time_div = event.find("div", class_="ng-tns-c8-2")
        court_div = (event.find("div", class_="text-muted text-small text-right ng-tns-c8-2 ng-star-inserted")).get_text(strip=True)
        court = court_div.split()[0].split("/")[1] if court_div else 0
        time_string = time_div.get_text(strip=True)

        #determine court count
        #TODO: may need revisiting with new scheduling
        if court in COURTS:
            court_count = COURTS[court]
        else:
            court_count = "TBD"

        #formatting each event for drop in poll
        EVENTS = { 
            "Advanced 2s Drop In": f"{weekday} ({time_string} ADV w/ {court_count})",
            "Intermediate 2s Drop In": f"{weekday} ({time_string} INT w/ {court_count})",
            "Intermediate 2s Drop In - Happy Hour": f"{weekday} ({time_string} INT w/ {court_count})",
            "Adult Level II/III Class": f"{weekday} ({time_string} lvl 2/3 class)",
            "Adult Level III Class": f"{weekday} ({time_string} lvl 3 class)",
            "Adult Level IV Class": f"{weekday} ({time_string} lvl 4 class)",
            "Adult Women's Level III Class": f"{weekday} ({time_string} Women's class)",
            "Sunday Skills": f"{weekday} ({time_string} Sunday Skills)"
        }

        if title in EVENTS and weekday in (INT_DROPIN_DAYS | ADV_DROPIN_DAYS | LVL3_DAYS | LVL4_DAYS | LVL2_3_DAYS | WOMENS_DAYS | SUNDAY_SKILLS):
            if weekday == "Wednesday" and ("1:00pm" in time_string or "9:00pm" in time_string):
                continue
            elif weekday == "Friday" and "8:00pm" in time_string:
                continue
            elif weekday == "Sunday" and ("1:00pm" in time_string or "3:00pm" in time_string):
                continue
            else:
                DROP_INS.append(EVENTS[title])
        