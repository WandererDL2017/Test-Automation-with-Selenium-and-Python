from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def cal(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  browser.get("http://suninjuly.github.io/explicit_wait2.html")

  price = WebDriverWait(browser, 11).until(
              EC.text_to_be_present_in_element((By.ID, "price"), "$100")
            )
  button = browser.find_element(By.ID, "book")
  button.click()

  x_element = browser.find_element(By.ID, "input_value")
  x = x_element.text
  result = cal(x)
  
  answer = browser.find_element(By.ID, "answer")
  answer.send_keys(result)
  time.sleep(1)
  
  button_submit = browser.find_element(By.ID, "solve")
  button_submit.click()
  
finally:
  time.sleep(10)
  browser.quit()
