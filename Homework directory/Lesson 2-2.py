from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service = service)
driver.maximize_window()

email= "Testemail@gmail.com"
password = "<PASSWORD>"

driver.get("https://www.target.com/")

driver.find_element(By.XPATH, "//div//span[contains"
                                     "(@class,'styles__LinkText-sc-1e1g60c-3')]").click()
# sleep(10)
driver.find_element(By.XPATH, "//div//ul//a[@data-test='accountNav-signIn']"
                              "//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl']").click()
sleep(10)
driver.find_element(By.XPATH, "//div[@class='styles__ContentWrapper-sc-19gc5cv-1 CpfGf']")
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.XPATH, "//div//input[@id='password']").send_keys(password)
sleep(5)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
sleep(10)
driver.quit()