from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')


driver.find_element(By.ID,"searchDropdownBox")

driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]')
driver.find_element(By.XPATH, '//input[@name="field-keywords"]')
driver.find_element(By.XPATH,"//select[contains(@class,'nav-search-dropdown searchSelect"
                             " nav-progressive-attrubute nav-progressive-search-dropdown')]")
driver.find_elements(By.XPATH,"//span[text()='Sign in for the best experience']")

sleep(5)