import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class TestGoogleSearch():
    def test_google_search(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.google.com/travel/flights")
        #driver.execute_scripts("window.open('https://www.google.com/travel/flights','_self');")

        time.sleep(2)
        driver.minimize_window()
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        driver.fullscreen_window()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.maximize_window()
        print(driver.title)
        ex_wait = WebDriverWait(driver, 20)

        #input departure
        ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Calgary']"))).click()
        time.sleep(3)
        ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Enter your origin']//div//input[@aria-label='Where else?']"))).send_keys("Van")
        time.sleep(4)
        list_departure = ex_wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='DFGgtd']//li//div[@class='CwL3Ec']//div[@class='w1ZvBc']")))
        for place in list_departure:
            if "Vancouver Island, British Columbia" in place.text:
                    place.click()
                    break # lam xong break lien
        time.sleep(2)

        # input arrival
        ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-placeholder= 'Where to?']//input[@placeholder='Where to?']"))).click()
        time.sleep(3)
        ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Enter your destination']//input"))).send_keys("Toro")
        time.sleep(3)
        list_arrival = ex_wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='DFGgtd']//li//div[@class='zsRT0d']")))
        time.sleep(3)
        for place in list_arrival:
            if "Toronto Pearson International Airport" in place.text:
                place.click()
                break
        time.sleep(2)

        # pickup way
        ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-hveid='CAEQBA']//div[@class='RLVa8 GeHXyb']"))).click()
        ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@aria-label='Select your ticket type.'][@role='listbox']//li[2]"))).click()
        
        #input number of customer
        ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Hj7hq LLHSpd']"))).click()
        ex_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='i5-2'] span[aria-live='polite']+ span"))).click()
        ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='IUKzPc']//button[@jsname='McfNlf']"))).click()
        #choose date

        #click search on how many stops

        #pay auto scroll

        #view more