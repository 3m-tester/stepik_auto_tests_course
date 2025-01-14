from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.CSS_SELECTOR, "input")

    for element in elements:
        element.send_keys("test")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # очікування, щоб візуально оцінити результати проходження скрипту
    time.sleep(10)
    # закриваємо браузер після всіх маніпуляцій:
    browser.quit()
