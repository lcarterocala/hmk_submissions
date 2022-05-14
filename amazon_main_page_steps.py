from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# list of locators
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
HAM_MENU_BTN = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, 'td.navFooterDescItem a')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_word}')
def search_amazon(context, search_word):
    context.driver.find_element(*SEARCH_INPUT).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()

@then('Verify hamburger menu btn present')
def verify_ham_menu(context):
    elements = context.driver.find_element(*HAM_MENU_BTN)
    assert len(elements) == 1, f'Error: Expected 1 item, but got {len(elements)}'


@then('Verify there are {expected_amount} footer links')
def verify_footer_links_count(context, expected_amount):
    expected_amount = int(expected_amount)
    footer_links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(footer_links) == expected_amount, f'Error: Expected {expected_amount} items, but got {len(footer_links)}'
