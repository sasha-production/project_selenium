import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import math
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    driver.get(link)
    WebDriverWait(driver, 12, poll_frequency=1).until(lambda d: d.find_element(By.ID, 'price').text == '$100')
    button = driver.find_element(By.ID, 'book')
    button.click()

    x = driver.find_element(By.ID, 'input_value')
    driver.execute_script("return arguments[0].scrollIntoView(true);", x)
    y = calc(x.text)
    input_field = driver.find_element(By.ID, 'answer')
    input_field.send_keys(y)
    submit_btn = driver.find_element(By.ID, 'solve')
    submit_btn.click()
    # button = driver.find_element(By.ID, "button")
    # button.click()

    # window_names = driver.window_handles
    # second_window = window_names[1]
    # driver.switch_to.window(second_window)
    #
    # x = driver.find_element(By.ID, 'input_value').text
    # y = calc(x)
    # input_field = driver.find_element(By.CSS_SELECTOR, '.form-group input.form-control')
    # input_field.send_keys(y)
    # button = driver.find_element(By.CSS_SELECTOR, ".container button")
    # button.click()
    # driver.switch_to.window(window_names[0])
finally:
    time.sleep(5)
    driver.quit()
