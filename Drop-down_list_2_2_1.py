from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")

    x = int(x_element.get_attribute("textContent"))
    y = int(y_element.get_attribute("textContent"))
    print(x, y)

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(x + y))
    print(x + y)

    # Натиснути на кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

finally:
    # очікування, щоб візуально оцінити результати проходження скрипта:
    time.sleep(10)
    # закриваємо браузер після всіх маніпуляцій:
    browser.quit()
