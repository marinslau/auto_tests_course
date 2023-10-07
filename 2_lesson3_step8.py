from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # нашли кнопку
    button = browser.find_element(By.ID, "book")

    # подождали пока цена не станет 100$
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    # кликнули кнопку
    button.click()

    # формула
    x_el = browser.find_element(By.ID, "input_value").text
    x = int(x_el)

    answer = calc(x)
    
    answer_el = browser.find_element(By.ID, "answer")
    answer_el.send_keys(answer)

    # отправляем
    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    time.sleep(10)
    browser.quit()