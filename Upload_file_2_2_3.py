from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ввести відповідь в текстове поле
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Aski")

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Lviv")

    # отримуємо шлях до директорії поточного файла, який зараз виконується!
    current_dir = os.path.abspath(
        os.path.dirname("c:\\Users\\Ruslan\\selenium_course\\text.txt")
    )
    # добавляємо до цього шляху ім'я файла
    file_path = os.path.join(current_dir, "text.txt")

    x_element = browser.find_element(By.ID, "file")
    x_element.send_keys(file_path)

    # Натиснути на кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # очікування, щоб візуально оцінити результати проходження скрипту
    time.sleep(10)
    # закриваємо браузер після всіх маніпуляцій:
    browser.quit()
