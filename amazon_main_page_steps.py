from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# list of locators
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
SEARCH_RESULTS = (By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
HAM_MENU_BTN = (By.ID, 'nav-hamburger-menu')
PRODUCT_TITLE = (By.CSS_SELECTOR, "h2 span.a-text-normal")
PRODUCT_IMG = (By.CSS_SELECTOR, "div.s-product-image-container")
FOOTER_LINKS = (By.CSS_SELECTOR, 'td.navFooterDescItem a')
SIGN_IN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")


@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main_page()


@when('Search for {search_word}')
def search_amazon(context, search_word):
    # context.driver.find_element(*SEARCH_INPUT).send_keys(search_word)
    # context.driver.find_element(*SEARCH_BTN).click()
    context.app.header.search_amazon(search_word)


@when('Click on button from SignIn popup')
def click_sign_in_btn(context):
    sign_in_btn = context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign In btn not clickable')
    sign_in_btn.click()


@when('Wait for {seconds} seconds')
def wait_sec(context, seconds):
    sleep(int(seconds))


@when('Click Amazon Orders link')
def click_amazon_orders_link(context):
    context.app.main_page.orders_link_click()


@then('Verify hamburger menu btn present')
def verify_ham_menu(context):
    elements = context.driver.find_element(*HAM_MENU_BTN)
    assert len(elements) == 1, f'Error: Expected 1 item, but got {len(elements)}'


@then('Verify there are {expected_amount} footer links')
def verify_footer_links_count(context, expected_amount):
    expected_amount = int(expected_amount)
    footer_links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(footer_links) == expected_amount, f'Error: Expected {expected_amount} items, but got {len(footer_links)}'


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Error! Title should not be blank'
        product.find_element(*PRODUCT_IMG)


@then('SignIn popup is present')
def verify_signin_popup_present(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn not clickable')


@then('SignIn popup disappears')
def verify_signin_popup_not_present(context):
    context.driver.wait.until_not(EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn did not disappear')
