from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):

    def sign_in_page_opened(self):
        self.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin?_encoding=UTF8&accountStatusPolicy'))

