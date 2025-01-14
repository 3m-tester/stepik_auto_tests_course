from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


# Dslrhbnb cnjhsyre по лінку:
link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Знайти на cnhfybwt елемент-картинку, який являється зображенням скрині зі скарбами
    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    # Взяти у цього елемента значення атрибута valuex, яке являється значенням x для задачі
    x = x_element.get_attribute("valuex")
    print(x)
    # Порахувати математичну функцію від x
    y = calc(x)

    # Ввести відповідь в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

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
    # очікування, щоб візуально оцінити результати проходження скрипту
    time.sleep(10)
    # закриваємо браузер після всіх маніпуляцій:
    browser.quit()
