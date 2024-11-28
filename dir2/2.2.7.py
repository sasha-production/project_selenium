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
    link = "https://suninjuly.github.io/file_input.html"
    browser.get(link)
    input_fields = browser.find_elements(By.CSS_SELECTOR, '.form-group input')
    for field in input_fields:
        field.send_keys('1')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'dir2\\2.2.7.txt')

    file_input = browser.find_element(By.CSS_SELECTOR, 'input[id=file]')
    file_input.send_keys(file_path)
    print(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(5)
    browser.quit()
