import requests
import build_poll

## TODO 
# - handle starting whats app connection without having to manually open dashboard
# - handle running this file 
# - handle running this file only on Sundays and Thursdays at 10am

API_URL = "http://localhost:3001/api/sendPoll"
API_KEY = "Cocopebbles215!"
SESSION = "default"  
CHAT_ID_GC = "120363369361790746@g.us"  
CHAT_ID = "18567459986@c.us"

###TODO make weekday/weekend date values dynamic and matching poll dates
WEEKDAY_DATES = "Drop Ins(11/22)"
WEEKEND_DATES = "Drop Ins(11/29 - 12/01)"



headers = {
    "X-Api-Key": API_KEY,
    "Content-Type": "application/json",
}

payload = {
  "chatId": CHAT_ID,
  "reply_to": None,
  "poll": {
    "name": WEEKDAY_DATES,
    "options": [
        "Yes",
        "No",
        "Maybe"
    ],
    "multipleAnswers": False,
  },
  "session": SESSION,
}

##main loop

try:
    response = requests.post(API_URL, json=payload, headers=headers)
    if response.status_code == 201:
        print("Poll sent successfully!")
        print("Response:", response.json())
    else:
        print(f"Failed to send poll. Status code: {response.status_code}")
        print("Response:", response.text)
except Exception as e:
    print("Error:", e)
