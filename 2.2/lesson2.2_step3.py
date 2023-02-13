from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def sum(num1, num2):
  return str(int(num1) + int(num2))

try:
  ## link = "https://suninjuly.github.io/selects1.html"
  link = "https://suninjuly.github.io/selects2.html"
  
  browser = webdriver.Chrome()
  browser.get(link)
  
  num1_element = browser.find_element(By.ID, "num1")
  num1 = num1_element.text
  num2_element = browser.find_element(By.ID, "num2")
  num2 = num2_element.text
  num3 = sum(num1, num2)
  time.sleep(1)
  
  select = Select(browser.find_element(By.TAG_NAME, "select"))
  select.select_by_value(num3)
  
  button = browser.find_element(By.CSS_SELECTOR, "button.btn")
  button.click()
  
finally:
  time.sleep(10)
  browser.quit()
  