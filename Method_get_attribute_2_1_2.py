from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Провіряємо значення атрибуту "required" у "I'm the robot".
    people_radio = browser.find_element_by_id("robotCheckbox")
    the_robot = people_radio.get_attribute("required")
    print("value of I'm the robot:", the_robot)
    assert the_robot is not None, "the_robot is not selected by default"

    # Провіряємо значення атрибуту checked у people_radio
    people_radio = browser.find_element(By.CSS_SELECTOR, "#peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people_radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    # Провіряємо значення атрибуту checked у robots_radio
    robots_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots_radio: ", robots_checked)
    assert robots_checked is None

    # Провіряємо значення атрибуту disabled у кнопки Submit
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit: ", button_disabled)
    assert button_disabled is None

    # Провіряємо значення атрибуту disabled у кнопки Submit після таймауту
    time.sleep(10)
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit after 10sec: ", button_disabled)
    assert button_disabled is not None

finally:
    # закриваємо браузер після всіх маніпуляцій:
    browser.quit()
