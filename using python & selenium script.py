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

driver.get('https://www.target.com/')
search_word = "coffee"
driver.find_element(By.ID,"search").send_keys(search_word)
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(6)
actual_result = driver.find_element(By.XPATH,"//div[@data-test='resultsHeading']").text

assert search_word in actual_result, f"Expected word {search_word} not in {search_word}"
print("Test is passed!! ")
driver.close()