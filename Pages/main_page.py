from Pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    SIGN_IN_NAV_TEXT = (By.XPATH, "//span[contains(@class,'styles__ListItemText') and text()='Sign in']")

    def open_main(self):
        self.open("https://www.target.com/")

    def verify_navigation_side_to_click_on_signin(self):
        self.wait_element_clickable_click(*self.SIGN_IN_NAV_TEXT)


