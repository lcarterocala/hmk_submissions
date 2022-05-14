from selenium.webdriver.common.by import By
from behave import given, when, then

# list of Locators
PRODUCT_1st = (By.XPATH, "//div[@data-component-type='s-search-result']//span[@class='a-price']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "input#add-to-cart-button")
CART_COUNT = (By.CSS_SELECTOR, "span#nav-cart-count")


@when('Cart is clicked')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a#nav-cart').click()


@when('Click on first product')
def click_on_first_product(context):
    context.driver.find_element(*PRODUCT_1st).click()


@when('Click on Add to Cart button')
def click_add_to_cart_btn(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@then('Results for cart are shown')
def cart_results(context):
    final_result = 'Your Amazon Cart is empty'
    real_result = context.driver.find_element(By.XPATH, "//h2").text
    assert final_result == real_result, f'Error! Actual test {real_result} does not match expected result {final_result}'


@then('Verify {expected_num} item(s) in cart')
def cart_results2(context, expected_num):
    cart_items = context.driver.find_element(*CART_COUNT).text
    cart_items = int(cart_items)
    expected_num = int(expected_num)
    assert cart_items == expected_num, f'Error: Expected {expected_num} items, but got {cart_items}'




    # experimental--section------
    # print(len(CART_COUNT))
    # print(type(CART_COUNT))
    # for i in CART_COUNT:
    #    print(i)


    # final_result = 'Your Amazon Cart is empty'
    # real_result = context.driver.find_element(By.XPATH, "//h2").text
    # assert final_result == real_result, f'Error! Actual test {real_result} does not match expected result {final_result}'



