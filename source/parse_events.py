from datetime import date

DROP_INS = []
## TODO: Edit based on new years schedule (Lvl 3/4 classes)
COURTS = {"16": "1 court", "32": "2 courts", "48": "3 courts"}
ADV_DROPIN_DAYS = {"Monday", "Saturday", "Sunday"}
INT_DROPIN_DAYS = {"Wednesday", "Thursday", "Sunday"}
LVL3_DAYS = {"Monday", "Wednesday", "Sunday"}
LVL4_DAYS = {"Thursday"}

def parse(events, weekday):
    for event in events:
        title = (event.find("h6", class_="flex-grow-1 text-truncate mb-0 mr-2")).text.strip()
        time_div = event.find("div", class_="ng-tns-c8-2")
        court_div = (event.find("div", class_="text-muted text-small text-right ng-tns-c8-2 ng-star-inserted")).get_text(strip=True)
        court = court_div.split()[0].split("/")[1] if court_div else 0
        time_string = time_div.get_text(strip=True)

        #determine court count
        if court in COURTS:
            court_count = COURTS[court]
        else:
            court_count = "TBD"

        EVENTS = { 
            "Advanced 2s Drop In": f"{weekday} ({time_string} ADV w/ {court_count})",
            "Intermediate 2s Drop In": f"{weekday} ({time_string} INT w/ {court_count})",
            "Intermediate 2s Drop In - Happy Hour": f"{weekday} ({time_string} INT w/ {court_count})",
            "Adult Level III Class": f"{weekday} ({time_string} lvl 3 class)",
            "Adult Level IV Class": f"{weekday} ({time_string} lvl 4 class)"
        }

        ##TODO: edit based on new naming conventions on website
        if title in EVENTS and weekday in (INT_DROPIN_DAYS | ADV_DROPIN_DAYS | LVL3_DAYS | LVL4_DAYS):
            if "8:00pm" not in time_string:
                DROP_INS.append(EVENTS[title])