from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Відкрити сторінку по лінку:
link = "http://suninjuly.github.io/redirect_accept.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    # Натиснути на кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Вибираємо другу вкладку
    new_window = browser.window_handles[1]
    # Переключити на нову вкладку
    browser.switch_to.window(new_window)

    element = browser.find_element(By.ID, "input_value")
    x = element.get_attribute("textContent")

    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Натиснути на кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # очікування, щоб візуально оцінити результати проходження скрипту
    time.sleep(10)
    # Щоб з модального вікна не копіпастити відповідь, можна вивести його в консоль
    print(browser.switch_to.alert.text)
    # закриваємо браузер після всіх маніпуляцій:
    browser.quit()
