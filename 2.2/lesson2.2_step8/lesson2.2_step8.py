from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
  link = "http://suninjuly.github.io/file_input.html"
  browser = webdriver.Chrome()
  browser.get(link)
  
  input_name = browser.find_element(By.XPATH, "//input[@placeholder = 'Enter first name']")
  input_name.send_keys("Денис")
  input_last_name = browser.find_element(By.XPATH, "//input[@placeholder='Enter last name']")
  input_last_name.send_keys("Денисов")
  input_email = browser.find_element(By.XPATH, "//input[@placeholder='Enter email']")
  input_email.send_keys("demo@demo")
  
  input_file = browser.find_element(By.ID, "file")
  current_dir = os.path.abspath(os.path.dirname(__file__))
  file_path = os.path.join(current_dir, "file.txt")
  input_file.send_keys(file_path)
  
  time.sleep(1)
  button = browser.find_element(By.CSS_SELECTOR, "button.btn")
  button.click()
  
finally:
  time.sleep(10)
  browser.quit()
  