from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
def calc(x):
 return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    wait = WebDriverWait(browser, 12)  # Создаём объект ожидания
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[id='price']"), "$100"))  # Ждём условие
    button = browser.find_element(By.CSS_SELECTOR, ".btn ")
    button.click()

#    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
#    x = int(x_element.text)
#    q = calc(x)
#    print(q)
#   z_element = browser.find_element(By.CSS_SELECTOR, '[id="num2"]')
#  z = int(z_element.text)
#    s = str(x + z)
#    print(s)


#    button = browser.find_element(By.CSS_SELECTOR, ".trollface ")
#    button.click()
    #   alert = browser.switch_to.alert
    #   alert.accept()

 #   new_window = browser.window_handles[1]
 #   browser.switch_to.window(new_window)

    Congratulations_locator = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    Congratulations = Congratulations_locator.text
    q = calc(Congratulations)
    input1 = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    print(q)
    input1.send_keys(q)

#    file = browser.find_element(By.CSS_SELECTOR, '[id="file"]')
 #   current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
  #  file_path = os.path.join(current_dir, 'new.txt')  # добавляем к этому пути имя файла
#    file.send_keys(file_path)

 #   input1 = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
 #   input1.send_keys('My answer')
 #   input1 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
 #   input1.send_keys('My answer2')
 #   input1 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
 #   input1.send_keys('My answer3')

#   check = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
#    check.click()

 #   radio = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
 #   browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
 #   radio.click()

    button = browser.find_element(By.CSS_SELECTOR, "[id='solve']")
    browser.execute_script("arguments[0].scrollIntoView(true);", button)

    #    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
#    y = calc(x)
#    print(y)
 #   select = Select(browser.find_element(By.CSS_SELECTOR, '.custom-select'))
 #   select.select_by_value(s)



    #   check = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
    #  check.click()

    #   radio = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
    #    radio.click()

#    submit = browser.find_element(By.CSS_SELECTOR, '.btn')
#    submit.click()

#    time.sleep(3)
#    Congratulations_locator = browser.find_element(By.TAG_NAME, "h1")
#    Congratulations = Congratulations_locator.text

 #   assert "Congratulations! You have successfully registered!" == Congratulations


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла