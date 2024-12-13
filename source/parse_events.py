from datetime import date

DROP_INS = []
COURTS = {"16": "1 court", "32": "2 courts", "48": "3 courts"}
ADV_DROPIN_DAYS = ["Monday", "Wednesday", "Saturday", "Sunday"]
INT_DROPIN_DAYS = ["Thursday", "Sunday"]
LVL3_DAYS = ["Tuesday", "Saturday", "Sunday"]

def parse(events, weekday):
    for event in events:
        title = (event.find("h6", class_="flex-grow-1 text-truncate mb-0 mr-2")).text.strip()
        print("TILE DIV IS -----------", title)
        time_div = event.find("div", class_="ng-tns-c8-2")
        court_div = (event.find("div", class_="text-muted text-small text-right ng-tns-c8-2 ng-star-inserted")).get_text(strip=True)
        court = court_div.split()[0].split("/")[1] if court_div else 0
        print("COURT DIV IS ---------", court)
        time_string = time_div.get_text(strip=True)

        #determine court count
        if court in COURTS:
            court_count = COURTS[court]
        else:
            court_count = "TBD"

        ##TODO use events to refactor below for loop
        EVENTS = { 
            "Advanced 2s Drop In": f"{weekday} ({time_string} ADV w/ {court_count})",
            "Intermediate 2s Drop In": f"{weekday} ({time_string} INT w/ {court_count})",
            "Adult Level III Class": f"{weekday} ({time_string} lvl 3 class)",
            "Level IV": f"{weekday} ({time_string} lvl 4 class)"
        }
        
        
        
        #add event data to drop in array with styling
        if "Advanced 2s Drop In" in title and weekday in ADV_DROPIN_DAYS:
            if "8:00pm" not in time_string:
                DROP_INS.append(f"{weekday} ({time_string} ADV w/ {court_count})")  
        if "Intermediate 2s Drop In" in title and weekday in INT_DROPIN_DAYS:
            DROP_INS.append(f"{weekday} ({time_string} INT w/ {court_count})")
        if "Adult Level III Class" in title and weekday in LVL3_DAYS:
            DROP_INS.append(f"{weekday} ({time_string} lvl 3 class)")
        if "Level IV" in title:
            DROP_INS.append(f"{weekday} ({time_string} lvl 4 class)")