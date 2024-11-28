import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import os

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, ".container button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    input_field = browser.find_element(By.CSS_SELECTOR, '.form-group input.form-control')
    input_field.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, ".container button")
    button.click()
finally:
    time.sleep(5)
    browser.quit()
