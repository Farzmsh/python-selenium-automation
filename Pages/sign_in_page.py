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

    def right_side_navigation_menu(self):
        self.wait_element_clickable_click(*self.SIGN_IN_NAV_TEXT)

    def verify_navigation_side_to_click_on_signin(self):
        self.wait_element_clickable_click(*self.SIGN_IN_NAV_TEXT)

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