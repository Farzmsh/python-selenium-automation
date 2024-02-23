
from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep


class CirclePage(Page):
    TABS = (By.CSS_SELECTOR, "[class*='PageSelectionText'] a")
    BONUS_TAB = (By.CSS_SELECTOR, "[data-test='bonus-tab']")

    def open_circle(self):
        self.open("https://www.target.com/circle")

    def verify_can_click_thru_tabs(self):
        self.wait_element_clickable(*self.BONUS_TAB)

        tabs = self.find_elements(*self.TABS)
        current_url = ''

        for i in range(len(tabs)):
            tabs = self.find_elements(*self.TABS)
            tabs[i].click()
            self.wait_url_changes(current_url)
            current_url = self.driver.current_url


