import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
url = 'https://suninjuly.github.io/selects2.html'
try:
    driver.get(url)

    num1 = driver.find_element(By.CSS_SELECTOR, 'h2 span[id=num1]')
    num2 = driver.find_element(By.CSS_SELECTOR, 'h2 span[id=num2]')
    res = int(num1.text) + int(num2.text)
    select = Select(driver.find_element(By.CSS_SELECTOR, 'select.custom-select'))

    select.select_by_value(str(res))

    # checkbox = driver.find_element(By.CSS_SELECTOR, 'input[id=robotCheckbox]')
    # checkbox.click()
    #
    # radiobutton = driver.find_element(By.CSS_SELECTOR, 'input[id=robotsRule]')
    # radiobutton.click()
    #
    submit = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    submit.click()

finally:
    time.sleep(5)
    driver.quit()
