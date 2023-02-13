from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
  browser = webdriver.Chrome()
  browser.get("http://suninjuly.github.io/find_xpath_form")
  elements = browser.find_elements(By.TAG_NAME, "input")
  for element in elements:
    element.send_keys("Мой ответ")
  
  buttons = browser.find_elements(By.XPATH, '//button[@type="submit"]')
  for button in buttons:
    button.click()
    
finally:
  time.sleep(30)
  browser.quit()
  