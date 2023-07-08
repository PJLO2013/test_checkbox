from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://demoqa.com/upload-download")

time.sleep(3)

btn_dwnld = driver.find_element(By.ID,"downloadButton").click()

time.sleep(5)