from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
sys.path.append("D:/Automation Testing/Selenium-Python---First-Project/Library")

driver = webdriver.Chrome()
driver.maximize_window()

# Buka halaman web
def openWeb():
    driver.get("https://zzzscore.com/1to50/en/")
    time.sleep(5)

# Play game
def playGame():
    grid = driver.find_element(By.XPATH, '//*[@class="resetBtn"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", grid)
    
    for i in range(1, 51):
        number = driver.find_element(By.XPATH, f'//*[@class="grid x5"]//div[text()="{i}"]')
        number.click()
        
    time.sleep(1)
    
    driver.quit()
