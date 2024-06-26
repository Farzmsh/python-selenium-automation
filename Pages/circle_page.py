
from selenium.webdriver.common.by import By
from Pages.base_page import Page
from time import sleep


class CirclePage(Page):
    TABS = (By.CSS_SELECTOR, "[class*='PageSelectionText'] a")
    BONUS_TAB = (By.CSS_SELECTOR, "[data-test='bonus-tab']")
    GOOGLE_PLAY_BTN = (By.CSS_SELECTOR, "[alt='Get it on Google Play']")


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

    def click_google_play_btn(self):
        self.wait_element_clickable_click(*self.GOOGLE_PLAY_BTN)

    def google_play_opened(self):
        self.verify_partial_url("https://play.google.com/store/apps/")
