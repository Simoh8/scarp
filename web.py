import time
from selenium import webdriver
from datetime import datetime
import time

PATH="C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

url = 'https://odibets.com/league'

driver.get(url)

while(True):
    now = datetime.now()
    
    # this is just to get the time at the time of
    # web scraping
    current_time = now.strftime("%H:%M:%S")
    print(f'At time : {current_time} IST')
    c = 1

    for x in range(3, 9):
        curr_path = ''
        
        # Exception handling to handle unexpected changes
        # in the structure of the website
        try:
            curr_path = f'//html/body/div/div[1]/div/div[2]/div[1]/div[2]'
            title = driver.find_element_by_xpath(curr_path)
        except:
            continue
        print(f"Heading {c}: ")
        c += 1
        print(title.text)
        
    # to stop the running of code for 10 mins
    time.sleep(600)
