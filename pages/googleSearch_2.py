import time
from selenium.webdriver.common.by import By
from base.base import BaseGoogleSearch


class googleSearch_2(BaseGoogleSearch):
    def __init__(self, driver):
        self.driver = driver

    def google_search_2(self):
        # click search on how many stops
        # self.ex_wait.until(EC.element_to_be_clickable(( By.XPATH, "//button[@aria-label= 'Stops, Not selected']"))).click()
        # b2
        BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//button[@aria-label= 'Stops, Not selected']").click()
        time.sleep(3)
        # 2 stop or a few
        self.driver.find_element(By.XPATH, "//input[@aria-label='2 stops or fewer']").click()
        # b2
        # BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//input[@aria-label='2 stops or fewer']").click()
        time.sleep(2)

        # Non-stop
        self.driver.find_element(By.XPATH, "//input[@aria-label='Nonstop only']").click()
        # b2

        time.sleep(3)
        # any stop
        self.driver.find_element(By.XPATH, "//input[@aria-label='Any number of stops']").click()
        # b2

        time.sleep(3)
        # 1 stop or a few
        self.driver.find_element(By.XPATH, "//input[@aria-label='1 stop or fewer']").click()
        # b2

        time.sleep(3)
        # clear on Stop
        self.driver.find_element(By.XPATH, "//span[text()='Clear']").click()
        # b2


        time.sleep(2)
        # close dialog tren stop
        self.driver.find_element(By.XPATH, "//div[@jsname='M7dhxe']//button[@aria-label='Close dialog']").click()
        # b2


        time.sleep(2)

        # #pay auto scroll
        # pagelength = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var pagelength = document.body.scrollHeight; return pagelength; ")
        # # b2
        #
        # flag = False
        # while flag == False:
        #     maxlength = pagelength
        #     pagelength = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var pagelength = document.body.scrollHeight; return pagelength;")
        #     # b2
        #
        #     if maxlength == pagelength:
        #         flag = True
        #
        # time.sleep(3)
        # view more
        # more_flights = self.ex_wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='ZVk93d']//button")))
        # b2
        more_flights = BaseGoogleSearch.base_element_to_be_clickable(self, By.XPATH, "//li[@class='ZVk93d']//button")

        more_flights.click()
        time.sleep(10)
