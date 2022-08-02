import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class TestGoogleSearch():
    def test_google_search(self):
        # 1. chuyen qua conftest
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
        ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@jsname='huwV5e']//input[@placeholder='Departure']"))).click()
        all_dates = ex_wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='SJyhnc bVf6m']//div[@role='rowgroup']//div[@jsname='mG3Az']")))
        for date in all_dates:
            if date.get_attribute("data-iso") == "2022-09-26":
                date.click()
                break
        ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@jsname='WCieBd']//span[@jsname='V67aGc']"))).click()


        #click search on how many stops
        ex_wait.until(EC.element_to_be_clickable(( By.XPATH, "//button[@aria-label= 'Stops, Not selected']"))).click()
        time.sleep(3)
        # 2 stop or a few
        driver.find_element(By.XPATH, "//input[@aria-label='2 stops or fewer']").click()
        time.sleep(2)
        # Non-stop
        driver.find_element(By.XPATH, "//input[@aria-label='Nonstop only']").click()
        time.sleep(3)
        # any stop
        driver.find_element(By.XPATH, "//input[@aria-label='Any number of stops']").click()
        time.sleep(3)
        # 1 stop or a few
        driver.find_element(By.XPATH, "//input[@aria-label='1 stop or fewer']").click()
        time.sleep(3)
        # clear on Stop
        driver.find_element(By.XPATH, "//span[text()='Clear']").click()
        time.sleep(2)
        # close dialog tren stop
        driver.find_element(By.XPATH, "//div[@jsname='M7dhxe']//button[@aria-label='Close dialog']").click()
        time.sleep(2)


        #pay auto scroll
        pagelength = driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var pagelength = document.body.scrollHeight; return pagelength; ")
        flag = False
        while flag == False:
            maxlength = pagelength
            pagelength = driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var pagelength = document.body.scrollHeight; return pagelength;")
            if maxlength == pagelength:
                flag = True


        #view more
        more_flights = ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='ZVk93d']//button")))
        more_flights.click()
        time.sleep(10)


        # 1. set up (contest) (*)
        # 2. loai bo ex-wait, element is clikable (base)
        # 3. chay trang tu dong (base)
        #
        # 4. trang dau
        # 5. trang cuoi
        #
        # 6.log (utilities)
        # 7. kiem tra du lieu ra (utilities)
        # 10.doc du lieu tu ngaoi vao (utilities)


        # 8. chay nhieu browers (conftest)
        # 9. reports ra sau (conftest)