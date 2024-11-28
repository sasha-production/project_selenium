import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
url = 'https://suninjuly.github.io/get_attribute.html'
try:
    driver.get(url)

    picture = driver.find_element(By.CSS_SELECTOR, 'img[id=treasure]')
    valuex = picture.get_attribute('valuex')
    y = calc(valuex)
    input_field = driver.find_element(By.ID, 'answer')
    input_field.send_keys(y)

    checkbox = driver.find_element(By.CSS_SELECTOR, 'input[id=robotCheckbox]')
    checkbox.click()

    radiobutton = driver.find_element(By.CSS_SELECTOR, 'input[id=robotsRule]')
    radiobutton.click()

    submit = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    submit.click()

finally:
    time.sleep(5)
    driver.quit()
