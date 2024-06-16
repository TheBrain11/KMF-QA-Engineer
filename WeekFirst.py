from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver_path = '/usr/bin/google-chrome'


driver = webdriver.Chrome()


try:

    driver.get('https://kmf.kz/products/kmf-dostar/')


    time.sleep(5)


    h2_element = driver.find_element(By.XPATH, "//h2[text()='Условия кредитования']")
    

    next_element = h2_element.find_element(By.XPATH, "following-sibling::*")


    print(next_element.text)

finally:

    driver.quit()
