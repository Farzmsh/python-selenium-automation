
from selenium.webdriver.common.by import By
from time import sleep
from Pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.XPATH, "//div[@data-test='@web/CartIcon']")
    SIGN_IN_TEXT = (By.XPATH, "//span[text()='Sign in']")

    def search_product(self):
        self.input_text('coffee',*self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(6)

    def click_cart_icon(self):
        self.wait_element_clickable_click(*self.CART_ICON)

    def click_sign_in_text(self):
        self.click(*self.SIGN_IN_TEXT)

