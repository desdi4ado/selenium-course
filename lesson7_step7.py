# поиск сокровища с помощью get_attribute
'''
Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".
'''

from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    img = browser.find_element_by_tag_name('img')
    x = img.get_attribute('valuex')
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    is_robot = browser.find_element_by_id('robotCheckbox')
    is_robot.click()

    robot_rule = browser.find_element_by_id('robotsRule')
    robot_rule.click()

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(5)
    browser.quit()