# Задание на execute_script
'''
Напишите код, который реализует следующий сценарий:

Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
'''

from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('input_value').text
    # num = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))

    is_robot = browser.find_element_by_id('robotCheckbox')
    is_robot.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    robot_rule = browser.find_element_by_id('robotsRule')
    robot_rule.click()

    button.click()

finally:
    time.sleep(20)
    browser.quit()