from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep


class TermsAndConditions(Page):
    def terms_and_conditions_open(self):
        self.verify_partial_url("https://www.target.com/c/terms-conditions/")
