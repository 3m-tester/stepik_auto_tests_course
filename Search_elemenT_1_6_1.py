from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

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
    time.sleep(20)
    # закриваємо браузер після всіх маніпуляцій:
    browser.quit()
