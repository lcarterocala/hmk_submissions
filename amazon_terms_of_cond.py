from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


PRIVACY_LINK = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")


@given('Open Amazon T&C page')
def open_terms_of_conditions_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')
    sleep(5)


@when('Store original windows')
def store_original_windows(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)
    print(context.driver.window_handles)


@when('Click on Amazon Privacy Notice link')
def click_privacy_link(context):
    context.driver.find_element(*PRIVACY_LINK).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print("\nAfter click, windows:", context.driver.window_handles)
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_amazon_privacy_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'))


@then('User can close new window')
def close_page_and_switch(context):
    context.driver.close()


@then('User can switch back to original')
def return_to_original(context):
    context.driver.switch_to.window(context.original_window)