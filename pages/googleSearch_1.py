import time
from selenium.webdriver.common.by import By
from base.base import BaseGoogleSearch
from pages.googleSearch_2 import googleSearch_2


class googleSearch_1(BaseGoogleSearch):
    def __init__(self, driver):
        self.driver = driver

    def google_search_1(self):
        # 2. loai bo ex-wait, element is clikable (base) + sua code o file chinh

        # input departure

        # self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Calgary']"))).click()
        # b2
        BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//input[@value='Calgary']").click()
        time.sleep(3)

        # b2
        # self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Enter your origin']//div//input[@aria-label='Where else?']"))).send_keys("Van")
        BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//div[@aria-label='Enter your origin']//div//input[@aria-label='Where else?']").send_keys("Van")
        time.sleep(4)

        # b2
        # list_departure = self.ex_wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='DFGgtd']//li//div[@class='CwL3Ec']//div[@class='w1ZvBc']")))
        list_departure = BaseGoogleSearch.base_presence_of_all_elements_located(self, By.XPATH, "//ul[@class='DFGgtd']//li//div[@class='CwL3Ec']//div[@class='w1ZvBc']")

        for place in list_departure:
            if "Vancouver Island, British Columbia" in place.text:
                place.click()
                break  # lam xong break lien
        time.sleep(2)

        # input arrival

        # self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-placeholder= 'Where to?']//input[@placeholder='Where to?']"))).click()
        # b2
        BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//div[@aria-placeholder= 'Where to?']//input[@placeholder='Where to?']").click()
        time.sleep(3)

        # self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Enter your destination']//input"))).send_keys("Toro")
        # b2
        BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//div[@aria-label='Enter your destination']//input").send_keys("Toro")
        time.sleep(3)
        # list_arrival = self.ex_wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='DFGgtd']//li//div[@class='zsRT0d']")))
        # b2
        list_arrival = BaseGoogleSearch.base_presence_of_all_elements_located(self, By.XPATH, "//ul[@class='DFGgtd']//li//div[@class='zsRT0d']")
        time.sleep(3)
        for place in list_arrival:
            if "Toronto Pearson International Airport" in place.text:
                place.click()
                break
        time.sleep(2)

        # pickup way
        # self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-hveid='CAEQBA']//div[@class='RLVa8 GeHXyb']"))).click()
        # b2
        BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//div[@data-hveid='CAEQBA']//div[@class='RLVa8 GeHXyb']").click()

        # self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@aria-label='Select your ticket type.'][@role='listbox']//li[2]"))).click()
        # b2
        BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//ul[@aria-label='Select your ticket type.'][@role='listbox']//li[2]").click()
        time.sleep(2)

        # input number of customer
        # self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Hj7hq LLHSpd']"))).click()
        # b2
        BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//div[@class='Hj7hq LLHSpd']").click()
        # self.ex_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='i5-2'] span[aria-live='polite']+ span"))).click()
        # b2
        BaseGoogleSearch.base_element_to_be_clickable(self, By.CSS_SELECTOR, "div[id='i5-2'] span[aria-live='polite']+ span").click()
        # self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='IUKzPc']//button[@jsname='McfNlf']"))).click()
        # b2
        BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//div[@class='IUKzPc']//button[@jsname='McfNlf']").click()
        time.sleep(2)
        # choose date
        # self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@jsname='huwV5e']//input[@placeholder='Departure']"))).click()
        # b2
        BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//div[@jsname='huwV5e']//input[@placeholder='Departure']").click()

        # all_dates = self.ex_wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='SJyhnc bVf6m']//div[@role='rowgroup']//div[@jsname='mG3Az']")))
        # b2
        all_dates = BaseGoogleSearch.base_presence_of_all_elements_located(self, By.XPATH, "//div[@class='SJyhnc bVf6m']//div[@role='rowgroup']//div[@jsname='mG3Az']")

        for date in all_dates:
            if date.get_attribute("data-iso") == "2022-09-26":
                date.click()
                break
        time.sleep(2)

        # 4 chuyen qua google_search_ 2
        # self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@jsname='WCieBd']//span[@jsname='V67aGc']"))).click()
        # b2
        BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//div[@jsname='WCieBd']//span[@jsname='V67aGc']").click()
        gs2 = googleSearch_2(self.driver)
        return gs2
