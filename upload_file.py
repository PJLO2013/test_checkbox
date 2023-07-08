from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://demoqa.com/upload-download")

time.sleep(3)

buscador = driver.find_element(by=By.ID, value="uploadFile").send_keys("C:/Users/PABLO/Documents/imagen_python/sampleFile.jpeg")


time.sleep(10)


