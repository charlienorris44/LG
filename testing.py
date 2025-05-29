from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

options.add_argument("--user-data-dir=/tmp/chrome-user-data")
options.add_argument("--headless")

driver = webdriver.Chrome()

driver.get("http://localhost:8080/")

username_input = driver.find_element(By.ID, 'lg-email')
username_input.send_keys("charlie.norris@gmail.com")
# email validation test


password_input = driver.find_element(By.ID, 'password')
password_input.send_keys("bad password")
# password validation test

login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')
login_button.click()

emailvalidation = driver.execute_script("return arguments[0].validity.patternMismatch;", username_input)

if emailvalidation:
    print("Email validation test passed")
    username_input.clear()
    username_input.send_keys("charlie.norris@landg.com")
else:
    print("Email validation test failed")

passwordvalidation = driver.execute_script("return arguments[0].validity.patternMismatch;", password_input)

if passwordvalidation:
    print("Password validation test passed")
    password_input.clear()
    password_input.send_keys("aaaaaaA**")
else:
    print("Password validation test failed")

login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')
login_button.click()

try:
    label = driver.find_element(By.XPATH, '//label[text()="Upload a file:"]')
    print("Login test passed")
except NoSuchElementException:
    print("Login test failed")

upload_element = driver.find_element(By.ID, 'fileInput')
filePath = "/Users/macbook/Projects/LG website/LG/images/LOGO.png"
upload_element.send_keys(filePath)
time.sleep(1)
upload_button = driver.find_element(By.XPATH, '//button[text()="Upload File"]')
upload_button.click()
print("Upload test passed")

time.sleep(5)
driver.quit()