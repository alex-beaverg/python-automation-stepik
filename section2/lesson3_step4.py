from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.TAG_NAME, "button").click()
    browser.switch_to.alert.accept()
    x1 = int(browser.find_element(By.ID, "input_value").text)
    text = calc(x1)
    browser.find_element(By.ID, "answer").send_keys(text)
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(10)
    browser.quit()

