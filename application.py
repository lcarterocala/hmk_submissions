from pages.bestsellers_page import BestSellersPage
from pages.cart_case_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.signIn_page import SignInPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.bestsellers_page = BestSellersPage(self.driver)
        self.cart_case_page = CartPage(self.driver)
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.signIn_page = SignInPage(self.driver)
