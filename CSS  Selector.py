from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service = service)
driver.maximize_window()

driver.get("https://www.amazon.com/")
sleep(15)

# by ID
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
# by class
driver.find_element(By.CSS_SELECTOR, ".nav-input")
# by tag ID class
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input")
# by tag and attribute
driver.find_element(By.CSS_SELECTOR, "[type='submit']")
# Contains
driver.find_element(By.CSS_SELECTOR, "[data-nav-digest*='3DfYDRQEn+aN']")
driver.find_element(By.CSS_SELECTOR, '[id="nav-link-accountList-nav-line-1"]').click()
# Find parent and child
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='privacy_notic']")




sleep(10)

driver.quit()




