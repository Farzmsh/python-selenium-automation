from Pages.main_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_search_results_correct(self,expected_results):
        self.verify_partial_text(expected_results,*self.SEARCH_RESULTS_HEADER)

    def verify_search_results_page_url(self,expected_part_url):
        self.verify_partial_url(expected_part_url)