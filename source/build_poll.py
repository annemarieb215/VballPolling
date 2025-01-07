from datetime import date, timedelta
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from parse_events import DROP_INS, parse

## TODO 
# - handle starting whats app connection without having to manually open dashboard
# - figure out why when opening docker waha image runs automaticaly
# - handle running this file 
# - handle running this file only on Sundays and Thursdays at 10am

API_URL = "http://localhost:3000/api/sendPoll"
API_KEY = "Cocopebbles215!"
SESSION = "default"  
TEST_CHAT_ID_GC = "120363369361790746@g.us" #TESTING FOR GC
CHAT_ID_GC = "120363305034812145@g.us" #ONLY USE IN PRODUCTION
CHAT_ID = "18567459986@c.us" #TESTING FOR MYSELF
HEADERS = {
  "X-Api-Key": API_KEY,
  "Content-Type": "application/json",
}

TODAY = date.today()
DAY = str(TODAY.strftime("%A"))
DAYS = [TODAY + timedelta(days=i) for i in range(5)]
FIRST_DAY, SECOND_DAY, THIRD_DAY, FOURTH_DAY = DAYS[1], DAYS[2], DAYS[3], DAYS[4]
DATES = [FIRST_DAY, SECOND_DAY, THIRD_DAY, FOURTH_DAY] if DAY == "Sunday" else [FIRST_DAY, SECOND_DAY, THIRD_DAY]
WEEKDAY_TITLE = f"Drop Ins({FIRST_DAY.month}/{FIRST_DAY.day} - {FOURTH_DAY.month}/{FOURTH_DAY.day})"
WEEKEND_TITLE = f"Drop Ins({FIRST_DAY.month}/{FIRST_DAY.day} - {THIRD_DAY.month}/{THIRD_DAY.day})" 
HEADER_DATES = WEEKDAY_TITLE if DAY == "Sunday" else WEEKEND_TITLE
#For testing purposes
# DATES = [TODAY + timedelta(5), TODAY + timedelta(6), TODAY + timedelta(7)]

for datie in DATES:
  #start chrome driver and parse events for specfic date
  try:
      START_URL = f"https://apps.daysmartrecreation.com/dash/x/#/online/qbksports/event-registration?date={datie}&facility_ids=1"
      driver = webdriver.Chrome()
      driver.get(START_URL)
      
      time.sleep(10)

      html = driver.page_source
      soup = BeautifulSoup(html, "html.parser")
      events = soup.find_all("div", class_="card w-100 mx-0 mb-3 px-0 shadow-sm ng-tns-c8-2 ng-star-inserted")
      parse(events, str(datie.strftime("%A")))

  finally:
      driver.quit()

### TODO add emojis
DROP_INS.append("Nopie👻")

#set up payload to be sent in main.py
PAYLOAD = {
  "chatId": CHAT_ID,
  "reply_to": None,
  "poll": {
    "name": HEADER_DATES,
    "options": DROP_INS,
    "multipleAnswers": True,
  },
  "session": SESSION,
}