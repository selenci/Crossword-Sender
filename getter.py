import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os

fileName = "puzzle.puz"

# Downloads and saves the crossword locally
def downloadCrossword():
    url = 'https://herbach.dnsalias.com/uc/uc' + time.strftime("%y%m%d", time.localtime()) + '.puz'
    r = urllib.request.urlretrieve(url, fileName)

def uploadCrossword():
    downloadCrossword()

    Options = webdriver.ChromeOptions()
    Options.add_argument('--headless')
    Options.add_argument('--no-sandbox')                             
    Options.add_argument('--disable-dev-shm-usage')

    # Uploads the crossword
    driver = webdriver.Chrome(options=Options, service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://downforacross.com/")
    path = os.getcwd()
    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(f"{path}/{fileName}")
    driver.find_element(By.ID, "unlistedRow").find_element(By.TAG_NAME, "label").click()
    driver.find_element(By.CLASS_NAME,'swal-button--confirm').click()

    # Waits for the upload to finish
    start_time = time.time()

    success = False
    while(time.time() - start_time < 10):
        if(len(driver.find_elements(By.CLASS_NAME, 'swal-icon--success__ring')) > 0):
            success = True
            break
        time.sleep(0.05)

    os.remove(fileName)
    driver.quit()

    return success