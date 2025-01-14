from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


try:

    # кажемо Selenium провіряти протягом 5 секунд, поки кнопка не стане клікабельною
    element1 = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button = browser.find_element(By.ID, "book")
    button.click()

    element2 = browser.find_element(By.ID, "input_value")
    x = element2.get_attribute("textContent")

    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Натиснути на кнопку "Submit"
    button = browser.find_element(By.ID, "solve")
    button.click()
finally:
    # очікування, щоб візуально оцінити результати проходження скрипту
    time.sleep(10)
    print(browser.switch_to.alert.text)
    # закриваємо браузер після всіх маніпуляцій:
    browser.quit()
