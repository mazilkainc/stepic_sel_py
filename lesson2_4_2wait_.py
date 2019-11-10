from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    wait = WebDriverWait(browser, 40).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button1 = browser.find_element_by_xpath('//button[@id="book"]')
    button1.click()
#    message = browser.find_element_by_id("verify_message")

#    assert "successful" in message.text
    browser.execute_script("window.scrollBy(0, 400);")
    x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
    x = x_element.text
#    print(x)
    y = calc(x)
#    print(y)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys("{}" .format(y))

    button2 = browser.find_element_by_xpath('//button[@type="submit"]')
    button2.click()

finally:
    time.sleep(30)
    browser.quit()
