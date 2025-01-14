from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, який заповнює обов'язкові поля
    input1 = browser.find_element(
        By.CSS_SELECTOR,
        "div.first_block div.form-group.first_class input.form-control.first",
    )
    input1.send_keys("Ivan")

    input2 = browser.find_element(
        By.CSS_SELECTOR,
        "div.first_block div.form-group.second_class input.form-control.second",
    )
    input2.send_keys("Aski")

    input3 = browser.find_element(
        By.CSS_SELECTOR,
        "div.first_block div.form-group.third_class input.form-control.third",
    )
    input3.send_keys("test")
    # Відправляємо заповнену форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяємо, що змогли зареєструватися
    # Очікуємо завантаження сторінки
    time.sleep(5)

    # знаходимо елемент, який містить текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записуємо в змінну welcome_text текст із елемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # за допомогою assert провіряємо, що очікуваний текст співпадає з текстом на сторінці сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # очікування, щоб візуально оцінити результати проходження скрипту
    time.sleep(10)
    # закриваємо браузер після всіх маніпуляцій:
    browser.quit()

###we can search using XPath: elements = browser.find_elements_by_xpath("//input[contains(@class, 'second') and @required]")
