# загрузка файла
'''
Напишите код, который реализует следующий сценарий:

В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
'''

from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_name('firstname')
    name.send_keys('Ivan')

    lastname = browser.find_element_by_name('lastname')
    lastname.send_keys('Des')

    email = browser.find_element_by_name('email')
    email.send_keys('Des@mail.kz')

    file = browser.find_element_by_name('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    file.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(20)
    browser.quit()