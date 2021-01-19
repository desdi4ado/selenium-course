# кликаем по checkboxes и radiobuttons (капча для роботов)
'''
Открыть страницу http://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit.
'''

from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    is_robot = browser.find_element_by_xpath('//label[@for="robotCheckbox"]')
    is_robot.click()

    robot_rule = browser.find_element_by_xpath('//label[@for="robotsRule"]')
    robot_rule.click()

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(5)
    browser.quit()