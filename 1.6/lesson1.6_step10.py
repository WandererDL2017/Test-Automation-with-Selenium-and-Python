from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
  link = "http://suninjuly.github.io/registration1.html"
  
  browser = webdriver.Chrome()
  browser.get(link)
  
  input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
  input1.send_keys("Иван")
  input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
  input2.send_keys("Иванов")
  input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
  input3.send_keys("demo@demo")
  
  time.sleep(5)
  button = browser.find_element(By.CSS_SELECTOR, "button.btn")
  button.click()
  
  time.sleep(1)
  welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
  welcome_text = welcome_text_elt.text
  assert "Congratulations! You have successfully registered!" == welcome_text

finally:
  time.sleep(10)
  browser.quit()
  