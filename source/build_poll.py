from datetime import date, timedelta
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from parse_events import DROP_INS, parse

## TODO 
# - handle starting whats app connection without having to manually open dashboard
# - handle running this file 
# - handle running this file only on Sundays and Thursdays at 10am

API_URL = "http://localhost:3000/api/sendPoll"
API_KEY = "Cocopebbles215!"
SESSION = "default"  
CHAT_ID_GC = "120363369361790746@g.us"  
CHAT_ID = "18567459986@c.us"

HEADERS = {
    "X-Api-Key": API_KEY,
    "Content-Type": "application/json",
}

TODAY = date.today()
FIRST_DAY = TODAY + timedelta(1)
SECOND_DAY = TODAY + timedelta(2)
THIRD_DAY = TODAY + timedelta(3)
FOURTH_DAY = TODAY + timedelta(4)
DATES = [FIRST_DAY, SECOND_DAY, THIRD_DAY]

def build_dynamic_dates():
    if TODAY is "Sunday": 
        HEADER_DATES = f"Drop Ins({FIRST_DAY.month}/{FIRST_DAY.day} - {FOURTH_DAY.month}/{FOURTH_DAY.day})"
        DATES.append(FOURTH_DAY)
    else:
        HEADER_DATES = f"Drop Ins({FIRST_DAY.month}/{FIRST_DAY.day} - {THIRD_DAY.month}/{THIRD_DAY.day})"  
    
    return HEADER_DATES

for datie in DATES:
  try:
      START_URL = f"https://apps.daysmartrecreation.com/dash/x/#/online/qbksports/event-registration?date={datie}&facility_ids=1"
      driver = webdriver.Chrome()
      driver.get(START_URL)
      
      # Wait for the page to load (adjust the wait time as needed)
      time.sleep(5)

      html = driver.page_source
      soup = BeautifulSoup(html, "html.parser")
      events = soup.find_all("div", class_="card w-100 mx-0 mb-3 px-0 shadow-sm ng-tns-c8-2 ng-star-inserted")
      parse(events, str(datie.strftime("%A")))

  finally:
      driver.quit()

DROP_INS.append('Nopie :)')

PAYLOAD = {
"chatId": CHAT_ID_GC,
"reply_to": None,
"poll": {
  "name": build_dynamic_dates(),
  "options": DROP_INS,
  "multipleAnswers": False,
},
"session": SESSION,
}
