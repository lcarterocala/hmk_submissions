from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# list of Locators
PRODUCT_1st = (By.XPATH, "//div[@data-component-type='s-search-result']//span[@class='a-price']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "input#add-to-cart-button")
CART_COUNT = (By.CSS_SELECTOR, "span#nav-cart-count")
PRODUCT_NAME = (By.CSS_SELECTOR, "h1[id='title']")
CART = (By.CSS_SELECTOR, "#nav-cart-count")
COLORS_LOC = (By.CSS_SELECTOR, "span[id*='color_name'] img[id*='inline']")
COLOR_ID = (By.ID, 'inline-twister-expanded-dimension-text-color_name')


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')
    sleep(5)


@when('Cart is clicked')
def click_cart(context):
    # context.driver.find_element(By.CSS_SELECTOR, 'a#nav-cart').click()
    context.app.cart_case_page.cart_icon_click()


@when('Click on the first product')
def click_on_first_product(context):
    context.app.cart_case_page.click_on_first_product()


@when('Click on Add to Cart button')
def click_add_to_cart_btn(context):
    # context.driver.find_element(*ADD_TO_CART_BTN).click()
    # sleep(1)
    context.app.cart_case_page.click_add_to_cart_btn2()


@when('Store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@then('Verify Your Shopping Cart is empty')
def verify_cart_is_empty(context):
    context.app.cart_case_page.verify_empty_cart()


@then('Results for cart are shown')
def cart_results(context):
    final_result = 'Your Amazon Cart is empty'
    real_result = context.driver.find_element(By.XPATH, "//h2").text
    assert final_result == real_result, f'Error! Actual test {real_result} does not match expected result {final_result}'


@then('Verify {expected_num} item(s) in cart')
def cart_results2(context, expected_num):
    # cart_items = context.driver.find_element(*CART_COUNT).text
    # cart_items = int(cart_items)
    # expected_num = int(expected_num)
    # assert cart_items == expected_num, f'Error: Expected {expected_num} items, but got {cart_items}'
    context.app.cart_case_page.verify_cart_items(expected_num)


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == actual_text, f'Expected {expected_count}, but got {actual_text} instead.'


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*PRODUCT_NAME).text
    assert context.product_name == actual_name, f'Expected {context.product_name}'


@then('Verify user can click through colors')
def verify_clicking_colors(context):
    expected_colors = ['Black', 'Solid Black', 'Navy', 'Multicolour']
    actual_colors = []
    colors_loc = context.driver.find_elements(*COLORS_LOC)
    for options in colors_loc:
        options.click()
        color_id = context.driver.find_element(*COLOR_ID).text
        # actual_colors == [color_id]
        print(color_id)
    assert actual_colors == expected_colors, f'Error: Expected {expected_colors}, but got {actual_colors}'







    # experimental--section------
    # print(len(CART_COUNT))
    # print(type(CART_COUNT))
    # for i in CART_COUNT:
    #    print(i)


    # final_result = 'Your Amazon Cart is empty'
    # real_result = context.driver.find_element(By.XPATH, "//h2").text
    # assert final_result == real_result, f'Error! Actual test {real_result} does not match expected result {final_result}'



