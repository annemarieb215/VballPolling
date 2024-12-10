from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
from datetime import date, timedelta

DROP_INS = []
CLICK_PATHS = []

# Handle dynamic dates for accurate url link
TODAY = date.today()
WEEKDAY = str(TODAY.strftime("%A"))
START_URL = f"https://apps.daysmartrecreation.com/dash/x/#/online/qbksports/event-registration?date={TODAY}&facility_ids=1"
NUM_OF_DAYS = 4 if WEEKDAY is "Thursday" else 5

def build_clickpaths():
    for i in range(1, NUM_OF_DAYS):
        day = (TODAY + timedelta(days=i)).day
        CLICK_PATHS.append(f"//button[contains(@aria-label, '{day}')]")

##TODO use events to refactor below for loop
EVENTS = ["Advanced 2s Drop In", "Intermediate 2s Drop In", "Adult Level III Class", "Level IV"]

###TODO add classes and maybe refactor with that add
def parse_dropin_data(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    events = soup.find_all("div", class_="card w-100 mx-0 mb-3 px-0 shadow-sm ng-tns-c8-2 ng-star-inserted")

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
            DROP_INS.append(f"{WEEKDAY} ({time_string} ADV w/ {court_count})")
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
            DROP_INS.append(f"{WEEKDAY} ({time_string} INT w/ {court_count})")
    print("DROP IN LIST IS ----------------", DROP_INS)
    
def run_click(driver, click_path):
    print(click_path)
    # Click the target element
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,  click_path))
    ).click()
    time.sleep(3)

def run():
    build_clickpaths()
    for i in range(len(CLICK_PATHS)):
        # Start the driver
        driver = webdriver.Chrome()
        driver.get(START_URL)
        run_click(driver, CLICK_PATHS[i])
        parse_dropin_data(driver)
        driver.quit()

    return DROP_INS


