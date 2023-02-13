from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def cal(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  link = "http://suninjuly.github.io/alert_accept.html"
  browser = webdriver.Chrome()
  browser.get(link)
  button = browser.find_element(By.CSS_SELECTOR, "button.btn")
  button.click()
  
  confirm = browser.switch_to.alert
  confirm.accept()
  
  x_element = browser.find_element(By.ID, "input_value")
  x = x_element.text
  result = cal(x)
  
  answer = browser.find_element(By.ID, "answer")
  answer.send_keys(result)
  
  time.sleep(1)
  button = browser.find_element(By.CSS_SELECTOR, "button.btn")
  button.click()

finally:
  time.sleep(10)
  browser.quit()
  