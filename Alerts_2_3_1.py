from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Відкрити сторінку по лінку:
link = "http://suninjuly.github.io/alert_accept.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    # Натиснути на кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    element = browser.find_element(By.ID, "input_value")
    x = element.get_attribute("textContent")

    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Натиснути на кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # time.sleep(1)

finally:
    # Очікування, щоб візуально оцінити результати проходження скрипта
    time.sleep(10)

    # Щоб з модального вікна не копипастити відповідь, можна виводити його в консольі не використовувати time.sleep:
    print(browser.switch_to.alert.text)
    # закриваємо браузер після всіх маніпуляцій
    browser.quit()
