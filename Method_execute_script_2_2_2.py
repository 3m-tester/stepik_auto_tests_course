from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Відкрити сторінку по лінку:
link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # зчитати значення для змінної x
    element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = element.get_attribute("textContent")

    y = calc(x)

    # Ввести відповідь в текстове поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # Проскролити сторінку вниз
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Відмітити checkbox "I'm the robot".
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    # Вибрати radiobutton "Robots rule!"
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    # Натиснути на кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

finally:
    # очікування, щоб візуально оцінити результати проходження скрипта:
    time.sleep(10)
    # закриваємо браузер після всіх маніпуляцій:
    browser.quit()
