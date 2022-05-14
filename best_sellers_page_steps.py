from selenium.webdriver.common.by import By
from behave import given, when, then


# list of locators
# HEADER_LINKS = (By.CSS_SELECTOR, 'div#CardInstance3FqO1YoMwEA-HN1VlCwHTg a')
HEADER_LINKS = (By.CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a')


@given('Open BestSellers page')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify there are {expected_num} header links')
def verify_links_count(context, expected_num):
    expected_num = int(expected_num)
    head_links = context.driver.find_elements(*HEADER_LINKS)
    assert len(head_links) == expected_num, f'Error: Expected {expected_num} items, but got {len(head_links)}'
