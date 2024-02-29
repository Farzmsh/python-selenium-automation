from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from time import sleep

from Pages.base_page import Page


class HelpPage(Page):
    HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    HEADER_TOPIC = (By.XPATH, "//h1[text()=' Current promotions']")
    HEADER = (By.XPATH, "//h1[text()=' {HEADER_TEXT}']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    def open_help_returns(self):
        self.open('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def verify_returns_opened(self):
        self.wait_element_visible(*self.HEADER_RETURNS)

    def select_topic(self, help_topic):
        dropdown_menu = self.find_element(*self.TOPIC_SELECTION)
        select = Select(dropdown_menu)
        select.select_by_value(help_topic)
        # topics_dd = self.find_element(*self.TOPIC_SELECTION)
        # select = Select(topics_dd)
        # select.select_by_value(help_topic)

    def verify_topic_opened(self):
        self.wait_element_visible(*self.HEADER_TOPIC)

    # Dynamic locator
    def _get_header_locator(self, expected_header_text):
        # [By.XPATH, "//h1[text()=' Returns']"]
        return [self.HEADER[0], self.HEADER[1].replace('{HEADER_TEXT}', expected_header_text)]

    def verify_header(self, expected_header_text):
        locator = self._get_header_locator(expected_header_text)
        print(locator)
        self.wait_element_visible(*locator)
