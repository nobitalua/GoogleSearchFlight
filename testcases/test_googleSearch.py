import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base import BaseGoogleSearch

from webdriver_manager.chrome import ChromeDriverManager

from pages.googleSearch_1 import googleSearch_1


@pytest.mark.usefixtures("setup")
class TestGoogleSearch():
    def test_google_search(self):
        gs1 = googleSearch_1(self.driver)
        gs2 = gs1.google_search_1()
        gs2.google_search_2()
        # 1. chuyen qua conftest
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # driver.get("https://www.google.com/travel/flights")
        # #driver.execute_scripts("window.open('https://www.google.com/travel/flights','_self');")
        #
        # time.sleep(2)
        # driver.minimize_window()
        # time.sleep(2)
        # driver.maximize_window()
        # time.sleep(2)
        # driver.fullscreen_window()
        # time.sleep(2)
        # driver.refresh()
        # time.sleep(2)
        # driver.maximize_window()
        # print(driver.title)
        # ex_wait = WebDriverWait(driver, 20)


        # # 2. loai bo ex-wait, element is clikable (base) + sua code o file chinh
        # 3 chuyen qua google_search_ 1

        # #input departure
        #
        # #self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Calgary']"))).click()
        # #b2
        # BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//input[@value='Calgary']").click()
        # time.sleep(3)
        # # b2
        # #self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Enter your origin']//div//input[@aria-label='Where else?']"))).send_keys("Van")
        # BaseGoogleSearch.base_element_to_be_clickable(self,By.XPATH, "//div[@aria-label='Enter your origin']//div//input[@aria-label='Where else?']").send_keys("Van")
        # time.sleep(4)
        # # b2
        # #list_departure = self.ex_wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='DFGgtd']//li//div[@class='CwL3Ec']//div[@class='w1ZvBc']")))
        # list_departure = BaseGoogleSearch.base_presence_of_all_elements_located(self, By.XPATH, "//ul[@class='DFGgtd']//li//div[@class='CwL3Ec']//div[@class='w1ZvBc']")
        # for place in list_departure:
        #     if "Vancouver Island, British Columbia" in place.text:
        #             place.click()
        #             break # lam xong break lien
        # time.sleep(2)
        #
        #
        # # input arrival
        #
        # #self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-placeholder= 'Where to?']//input[@placeholder='Where to?']"))).click()
        # # b2
        # BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//div[@aria-placeholder= 'Where to?']//input[@placeholder='Where to?']").click()
        # time.sleep(3)
        #
        # #self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Enter your destination']//input"))).send_keys("Toro")
        # # b2
        # BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//div[@aria-label='Enter your destination']//input").send_keys("Toro")
        #
        # time.sleep(3)
        # #list_arrival = self.ex_wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='DFGgtd']//li//div[@class='zsRT0d']")))
        # # b2
        # list_arrival = BaseGoogleSearch.base_presence_of_all_elements_located(self, By.XPATH, "//ul[@class='DFGgtd']//li//div[@class='zsRT0d']")
        # time.sleep(3)
        # for place in list_arrival:
        #     if "Toronto Pearson International Airport" in place.text:
        #         place.click()
        #         break
        # time.sleep(2)
        #
        #
        # # pickup way
        # #self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-hveid='CAEQBA']//div[@class='RLVa8 GeHXyb']"))).click()
        # # b2
        # BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//div[@data-hveid='CAEQBA']//div[@class='RLVa8 GeHXyb']").click()
        #
        # #self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@aria-label='Select your ticket type.'][@role='listbox']//li[2]"))).click()
        # # b2
        # BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//ul[@aria-label='Select your ticket type.'][@role='listbox']//li[2]").click()
        # time.sleep(2)
        #
        # #input number of customer
        # #self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Hj7hq LLHSpd']"))).click()
        # # b2
        # BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//div[@class='Hj7hq LLHSpd']").click()
        # #self.ex_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='i5-2'] span[aria-live='polite']+ span"))).click()
        # # b2
        # BaseGoogleSearch.base_element_to_be_clickable(self, By.CSS_SELECTOR, "div[id='i5-2'] span[aria-live='polite']+ span").click()
        # #self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='IUKzPc']//button[@jsname='McfNlf']"))).click()
        # # b2
        # BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//div[@class='IUKzPc']//button[@jsname='McfNlf']").click()
        # time.sleep(2)
        # #choose date
        # #self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@jsname='huwV5e']//input[@placeholder='Departure']"))).click()
        # # b2
        # BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//div[@jsname='huwV5e']//input[@placeholder='Departure']").click()
        # #all_dates = self.ex_wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='SJyhnc bVf6m']//div[@role='rowgroup']//div[@jsname='mG3Az']")))
        # # b2
        # all_dates = BaseGoogleSearch.base_presence_of_all_elements_located(self, By.XPATH, "//div[@class='SJyhnc bVf6m']//div[@role='rowgroup']//div[@jsname='mG3Az']")
        # for date in all_dates:
        #     if date.get_attribute("data-iso") == "2022-09-26":
        #         date.click()
        #         break
        # time.sleep(2)



        # #4 chuyen qua google_search_ 2
        # #self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@jsname='WCieBd']//span[@jsname='V67aGc']"))).click()
        # # b2
        # BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//div[@jsname='WCieBd']//span[@jsname='V67aGc']").click()
        # #click search on how many stops
        # #self.ex_wait.until(EC.element_to_be_clickable(( By.XPATH, "//button[@aria-label= 'Stops, Not selected']"))).click()
        # # b2
        # BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//button[@aria-label= 'Stops, Not selected']").click()
        # time.sleep(3)
        # # 2 stop or a few
        # self.driver.find_element(By.XPATH, "//input[@aria-label='2 stops or fewer']").click()
        # # b2
        # #BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//input[@aria-label='2 stops or fewer']").click()
        # time.sleep(2)
        #
        # # Non-stop
        # self.driver.find_element(By.XPATH, "//input[@aria-label='Nonstop only']").click()
        # # b2
        #
        # time.sleep(3)
        # # any stop
        # self.driver.find_element(By.XPATH, "//input[@aria-label='Any number of stops']").click()
        # # b2
        #
        # time.sleep(3)
        # # 1 stop or a few
        # self.driver.find_element(By.XPATH, "//input[@aria-label='1 stop or fewer']").click()
        # # b2
        #
        # time.sleep(3)
        # # clear on Stop
        # self.driver.find_element(By.XPATH, "//span[text()='Clear']").click()
        # # b2
        #
        #
        # time.sleep(2)
        # # close dialog tren stop
        # self.driver.find_element(By.XPATH, "//div[@jsname='M7dhxe']//button[@aria-label='Close dialog']").click()
        # # b2
        #
        #
        # time.sleep(2)
        #
        #
        # # #pay auto scroll
        # # pagelength = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var pagelength = document.body.scrollHeight; return pagelength; ")
        # # # b2
        # #
        # # flag = False
        # # while flag == False:
        # #     maxlength = pagelength
        # #     pagelength = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var pagelength = document.body.scrollHeight; return pagelength;")
        # #     # b2
        # #
        # #     if maxlength == pagelength:
        # #         flag = True
        # #
        # #time.sleep(3)
        # #view more
        # #more_flights = self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='ZVk93d']//button")))
        # # b2
        # more_flights = BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//li[@class='ZVk93d']//button")
        #
        # more_flights.click()
        # time.sleep(10)


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