from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    browser.find_element(By.ID, "book").click()

    x1 = int(browser.find_element(By.ID, "input_value").text)
    text = calc(x1)
    browser.find_element(By.ID, "answer").send_keys(text)
    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(10)
    browser.quit()

