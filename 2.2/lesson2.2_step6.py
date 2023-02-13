from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def cal(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  link = "http://SunInJuly.github.io/execute_script.html"
  browser = webdriver.Chrome()
  browser.get(link)
  
  x_element = browser.find_element(By.ID, "input_value")
  x = x_element.text
  result = cal(x)
  
  input = browser.find_element(By.ID, "answer")
  browser.execute_script("return arguments[0].scrollIntoView(true);", input)
  input.send_keys(result)
  checkbox = browser.find_element(By.ID, "robotCheckbox")
  browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
  checkbox.click()
  radiobutton = browser.find_element(By.ID, "robotsRule")
  browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
  radiobutton.click()
  
  time.sleep(1)
  
  button = browser.find_element(By.CSS_SELECTOR, "button.btn")
  browser.execute_script("return arguments[0].scrollIntoView(true);", button)
  button.click()
  
finally:
  time.sleep(10)
  browser.quit()
  