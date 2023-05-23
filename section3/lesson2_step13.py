"""
Run with PyTest:
    pytest -s -v lesson2_step13.py
    pytest -s -v --browser_name=firefox lesson2_step13.py
    pytest -s -v --browser_name=chrome lesson2_step13.py
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


def test_registration1(browser):
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser.maximize_window()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Alex")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Popovko")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("a.popovko@mail.app")
        browser.find_element(By.CSS_SELECTOR, ".second_block .first").send_keys("+111(22)333-44-55")
        browser.find_element(By.CSS_SELECTOR, ".second_block .second").send_keys("address")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text

        assert welcome_text == "Congratulations! You have successfully registered!", \
            "Expected text on Registration page 1 was not found"
    finally:
        browser.quit()


def test_registration2(browser):
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser.maximize_window()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Alex")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Popovko")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("a.popovko@mail.app")
        browser.find_element(By.CSS_SELECTOR, ".second_block .first").send_keys("+111(22)333-44-55")
        browser.find_element(By.CSS_SELECTOR, ".second_block .second").send_keys("address")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text

        assert welcome_text == "Congratulations! You have successfully registered!", \
            "Expected text on Registration page 2 was not found"
    finally:
        browser.quit()


if __name__ == '__main__':
    unittest.main()