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
sleep(10)

driver.find_element(By.CSS_SELECTOR, '[id="nav-link-accountList-nav-line-1"]').click()
email_address = "Test@gmail.com"


driver.find_element(By.XPATH,"//div[@class='a-section a-spacing-none auth-navbar'] "
                             "//i[contains(@class,'a-icon')]")
print("Find the Amazon logo")

# driver.find_element(By.ID,"ap_email").send_keys(email_address)
# print("Find the Email")

condition_of_use = driver.find_element(By.XPATH,"//div[@id='legalTextRow'] "
                                                "//*[text()='Conditions of Use']").text
assert "Conditions of Use" in condition_of_use, f"Conditions of Use not found in {condition_of_use}"
# privacy_notice = driver.find_element(By.XPATH,"//div[@id='legalTextRow'] "
#                                               "//*[text()='Privacy Notice']").text
# assert privacy_notice == "Privacy Notice",f"Privacy Notice not in {privacy_notice}"
#
# need_help = driver.find_element(By.XPATH,"//div[@class='a-section']"
#                                          "//span[@class='a-expander-prompt']").text
# assert need_help == "Need help?",f"Need help? not in {need_help}"
#
# forgot_password= driver.find_element(By.XPATH,"//div[contains(@class,'a-expander-content')]"
#                                               "/a[@id='auth-fpp-link-bottom']").text
# assert "Forgot your password?" not in forgot_password,f"Forgot your password not in {forgot_password}"
#
# other_issue = driver.find_element(By.XPATH, "//div[contains(@class,'a-expander-content')]/a[@id='ap-other-signin-issues-link']").text
# assert "Other issues with Sign-In" not in other_issue, f'Other issues with Sign-In not in {other_issue}'
#
#
# driver.find_element(By.XPATH,"//span[@class='a-button-inner']//a[@id='createAccountSubmit']").click()
# driver.find_element(By.XPATH,"//input[@id='continue']").click()
# print("Find the Email field")


sleep(10)

driver.quit()




