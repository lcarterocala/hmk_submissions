from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# list of locators

@when('Hover over New Arrivals')
def hover_new_arrivals(context):
    context.app.product_details_page.hover_new_arrivals()


@then('Verify that user sees deals')
def verify_deals(context):
    context.app.product_details_page.verify_deals()
