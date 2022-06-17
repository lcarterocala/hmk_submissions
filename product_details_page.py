from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from pages.base_page import Page


class ProductDetailsPage(Page):

    NEW_ARRIVALS_LINK = (By.XPATH, "//a[contains(@href, '/New-Arrivals/b')]")
    DEALS = (By.CSS_SELECTOR, '.mega-menu')

    def hover_new_arrivals(self):
        actions = ActionChains(self.driver)
        new_arrivals_link = self.find_element(*self.NEW_ARRIVALS_LINK)
        actions.move_to_element(new_arrivals_link)
        actions.perform()

    def verify_deals(self):
        self.wait_for_element_appear(*self.DEALS)
