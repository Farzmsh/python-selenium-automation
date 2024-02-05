from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service = service)
driver.maximize_window()

driver.get("https://www.amazon.com")
name="User_name"
mobile="703000000"
pasword = "Password"


sleep(10)

driver.find_element(By.CSS_SELECTOR, '[id="nav-link-accountList-nav-line-1"]').click()

driver.find_element(By.CSS_SELECTOR, ".a-section .a-link-nav-icon")

driver.find_element(By.CSS_SELECTOR, "#createAccountSubmit.a-button-text").click()

driver.find_element(By.CSS_SELECTOR, "#ap_customer_name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#ap_email").send_keys(mobile)
driver.find_element(By.CSS_SELECTOR, "#ap_password").send_keys(pasword)
driver.find_element(By.CSS_SELECTOR, "#ap_password_check").send_keys(pasword)

driver.find_element(By.CSS_SELECTOR, "span.a-button-inner input[id=continue]").click()


driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href*='signin']")

sleep(5)
driver.quit()
