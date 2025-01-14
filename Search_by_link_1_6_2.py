from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link1 = browser.find_element(By.PARTIAL_LINK_TEXT, "224592")
    link1.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Aski")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Lviv")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Ukraine")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # очікування, щоб візуально оцінити результати проходження скрипту
    time.sleep(10)
    # закриваємо браузер після всіх маніпуляцій:
    browser.quit()
