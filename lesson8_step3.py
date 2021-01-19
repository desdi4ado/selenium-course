# работа с выпадающим списком
'''
Напишите код, который реализует следующий сценарий:

Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    find_sum = int(num1) + int(num2)
       
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(find_sum))

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(5)
    browser.quit()