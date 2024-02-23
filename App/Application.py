
from Pages.base_page import Page
from Pages.header import Header
from Pages.main_page import MainPage
from Pages.search_results_page import SearchResultsPage
from Pages.cart_page import CartPage
from Pages.circle_page import CirclePage
from Pages.sign_in_page import LoginPage, LoginPage


class Application:
    def __init__(self,driver):
        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.circle_page = CirclePage(driver)
        self.sign_in_page = LoginPage(driver)



