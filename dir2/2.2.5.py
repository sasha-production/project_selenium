import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



browser = webdriver.Chrome()
try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, '.form-group span:nth-child(2)').text
    y = calc(x)
    input_field = browser.find_element(By.CSS_SELECTOR, '.form-group input.form-control')
    button = browser.find_element(By.TAG_NAME, "button")
    input_field.send_keys(y)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element(By.CSS_SELECTOR, '.form-check-custom label')
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, 'input[id=robotsRule]')
    radiobutton.click()

    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(5)
    browser.quit()
