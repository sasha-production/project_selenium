import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
url = 'https://suninjuly.github.io/math.html'
try:
    driver.get(url)

    x = driver.find_element(By.CSS_SELECTOR, '.form-group span[id=input_value]')
    f_x = calc(x.text)
    input_field = driver.find_element(By.CSS_SELECTOR, 'input[id=answer]')
    input_field.send_keys(f_x)

    checkbox = driver.find_element(By.CSS_SELECTOR, 'input.form-check-input')
    checkbox.click()
    radiobutton = driver.find_element(By.CSS_SELECTOR, '.form-radio-custom input')
    radiobutton.click()

    submit = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    submit.click()

finally:
    time.sleep(5)
    driver.quit()
