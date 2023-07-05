from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://demoqa.com/webtables")

time.sleep(3)

btn_delete = driver.find_element(By.CSS_SELECTOR,"#delete-record-1 > svg > path").click()

time.sleep(3)

btn_add = driver.find_element(By.ID,"addNewRecordButton").click()

time.sleep(3)

Fname=driver.find_element(By.ID,"firstName")
Fname.send_keys("Pablo")

time.sleep(3)

Lname = driver.find_element(By.ID,"lastName")
Lname.send_keys("López")

time.sleep(3)

email = driver.find_element(By.ID,"userEmail")
email.send_keys("pablo@email.com")

time.sleep(3)

age = driver.find_element(By.ID,"age")
age.send_keys("33")

time.sleep(3)

salary = driver.find_element(By.ID,"salary")
salary.send_keys("50000")

time.sleep(3)

dept = driver.find_element(By.ID,"department")
dept.send_keys("TI")

btn_submit = driver.find_element(By.ID,"submit").click()

time.sleep(5)


