import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class", autouse = True)
def setup(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.google.com/travel/flights")
    # driver.execute_scripts("window.open('https://www.google.com/travel/flights','_self');")

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
    request.cls.driver = driver

    #chuyen ex_wait qua base class
    # ex_wait = WebDriverWait(driver, 20)
    # request.cls.ex_wait = ex_wait
    yield
    driver.close()