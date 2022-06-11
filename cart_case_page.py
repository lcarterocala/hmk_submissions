from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):

    PRODUCT_1st = (By.XPATH, "//div[@data-component-type='s-search-result']//span[@class='a-price']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "input#add-to-cart-button")
    CART_COUNT = (By.CSS_SELECTOR, "span#nav-cart-count")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1[id='title']")
    CART = (By.CSS_SELECTOR, "#nav-cart-count")
    COLORS_LOC = (By.CSS_SELECTOR, "span[id*='color_name'] img[id*='inline']")
    COLOR_ID = (By.ID, 'inline-twister-expanded-dimension-text-color_name')

    def cart_icon_click(self):
        self.click(*self.CART)

    def verify_empty_cart(self):
        final_result = 'Your Amazon Cart is empty'
        real_result = self.driver.find_element(By.XPATH, "//h2").text
        assert final_result == real_result, \
            f'Error! Actual test {real_result} does not match expected result {final_result}'

    def click_on_first_product(self):
        prod_c = self.driver.find_element(*self.PRODUCT_1st)
        prod_c.click()

    def click_add_to_cart_btn2(self):
        cart_add_btn = self.ADD_TO_CART_BTN
        crt_btn = self.driver.wait.until(EC.element_to_be_clickable(cart_add_btn), 'button not clickable')
        crt_btn.click()


    def verify_cart_items(self, expected_num):
        cart_items = self.driver.find_element(*self.CART_COUNT).text
        cart_items = int(cart_items)
        expected_num = int(expected_num)
        assert cart_items == expected_num, f'Error: Expected {expected_num} items, but got {cart_items}'

