from selenium.webdriver.common.by import By

from pages.base_page import Page


class Header(Page):
    # implement methods specific for headers
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')

    def search_amazon(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)
