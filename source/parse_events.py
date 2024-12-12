from datetime import date

DROP_INS = []

##TODO use events to refactor below for loop
EVENTS = ["Advanced 2s Drop In", "Intermediate 2s Drop In", "Adult Level III Class", "Level IV"]

##TODO add classes and maybe refactor with that add
def parse(events, weekday):
    for event in events:
        title = event.find("h6", class_="flex-grow-1 text-truncate mb-0 mr-2")
        time_div = event.find("div", class_="ng-tns-c8-2")
        courts = event.find("div", class_="text-muted text-small text-right ng-tns-c8-2 ng-star-inserted")
        if "Advanced 2s Drop In" in title.text.strip():
            time_string = time_div.get_text(strip=True)
            if "16" in courts.get_text(strip=True):
                court_count = "1 court"
            elif "32" in courts.get_text(strip=True):
                court_count = "2 courts"
            elif "48" in courts.get_text(strip=True):
                court_count = "3 courts"
            else:
                court_count = "TBD"
            DROP_INS.append(f"{weekday} ({time_string} ADV w/ {court_count})")
        if "Intermediate 2s Drop In" in title.text.strip():
            time_string = time_div.get_text(strip=True)
            if "16" in courts.get_text(strip=True):
                court_count = "1 court"
            elif "32" in courts.get_text(strip=True):
                court_count = "2 courts"
            elif "48" in courts.get_text(strip=True):
                court_count = "3 courts"
            else:
                court_count = "TBD"
            DROP_INS.append(f"{weekday} ({time_string} INT w/ {court_count})")
        ##TODO add classes and maybe refactor with that add





