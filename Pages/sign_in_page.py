from selenium.webdriver.common.by import By
from time import sleep
from Pages.base_page import Page


class LoginPage(Page):
    SIGN_IN_NAV_TEXT = (By.XPATH, "//span[contains(@class, 'ListItemText-sc-diphzn')] [text()='Sign in']")
    MY_USER_NAME = "tymmaksim@gpaemail.eu"
    MY_PASSWORD = "PASSWORD123"
    USER_NAME = (By.CSS_SELECTOR, "#username")
    PASSWORD = (By.CSS_SELECTOR,"#password")
    SIGNIN_BUTTON = (By.CSS_SELECTOR, "#login")
    TERM_CONDITIONS = (By.XPATH, "//a[text()='Target terms and conditions']")
    ENTER_VALID_PASSWORD = (By.XPATH, "//span[@id='password--ErrorMessage' and text()='Please enter a valid password']")
    INCORRECT_EMAIL = "Tommmmmy@gmail.com"
    INCORRECT_PASSWORD = "password"
    INVALID_ADDRESS = (By.XPATH, "//span[@id='password--ErrorMessage' and text()='Please enter a valid password']")

    # SIGN_IN_STEPS = (By.CSS_SELECTOR, "{sign_in_text}")

    # def get_sign_in_locator(self,expected_text):
    #     return self.SIGN_IN_STEPS[0], self.SIGN_IN_STEPS[1].replace("{sign_in_text}",expected_text)
    #
    # def sign_in_steps(self,email):
    #     locator = self.get_sign_in_locator(email)
    #     print(locator)
    #     self.find_element(*locator).send_keys(*self.INCORRECT_EMAIL)

    def right_side_navigation_menu(self):
        self.wait_element_clickable_click(*self.SIGN_IN_NAV_TEXT)

    # def verify_navigation_side_to_click_on_signin(self):
    #     self.wait_element_clickable_click(*self.SIGN_IN_NAV_TEXT)

    def user_user_name(self):
        self.find_element(*self.USER_NAME).send_keys(*self.MY_USER_NAME)
        sleep(6)

    def password(self):
        self.find_element(*self.PASSWORD).send_keys(*self.MY_PASSWORD)
        sleep(6)

    def sign_in_button(self):
        self.click(*self.SIGNIN_BUTTON)
        sleep(6)

    def click_on_target_terms_and_conditions(self):
        self.click(*self.TERM_CONDITIONS)
        sleep(6)

    def input_incorrect_email(self):
        self.find_element(*self.USER_NAME).send_keys(*self.INCORRECT_EMAIL)
        sleep(6)

    def input_incorrect_password(self):
        self.find_element(*self.PASSWORD).send_keys(*self.INCORRECT_PASSWORD)
        sleep(6)

    def verify_incorrect_email(self):
        self.find_element(*self.INVALID_ADDRESS)


