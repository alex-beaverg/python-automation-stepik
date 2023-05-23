import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

nlo_message = ''


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    print(nlo_message)
    browser.quit()


@pytest.mark.parametrize('link_path', [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
])
def test_login_stepik(browser, link_path):
    global nlo_message
    browser.get(link_path)
    browser.find_element(By.ID, "ember33").click()
    browser.find_element(By.NAME, 'login').send_keys('my email')
    browser.find_element(By.NAME, 'password').send_keys('my password')
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(str(math.log(int(time.time()))))
    browser.find_element(By.CSS_SELECTOR, 'button[class=submit-submission]').click()
    message = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
    if message != 'Correct!':
        nlo_message += message
    browser.find_element(By.CSS_SELECTOR, '.again-btn').click()


if __name__ == "__main__":
    unittest.main()
