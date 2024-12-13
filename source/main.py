import requests
from build_poll import PAYLOAD, API_URL, HEADERS

#send request to WhatsApp API and post poll
try:
    response = requests.post(API_URL, json=PAYLOAD, headers=HEADERS)
    if response.status_code == 201:
        print("Poll sent successfully!")
        print("Response:", response.json())
    else:
        print(f"Failed to send poll. Status code: {response.status_code}")
        print("Response:", response.text)
except Exception as e:
    print("Error:", e)