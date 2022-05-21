from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service




# init driver
s = Service('C:\\Users\\carte\\Automation\\python-selenium-automation\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# driver = webdriver.Chrome(executable_path='C:/Users/carte/Automation/python-selenium-automation/chromedriver.exe')
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

# Locators - CSS & XPATH practice
# CSS-Amazon logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon-logo')

# CSS-The Create Account Logo
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# CSS-customer name input box
driver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name')

# CSS-mobile number or email input
driver.find_element(By.CSS_SELECTOR, 'input#ap_email')

# CSS-password input box
driver.find_element(By.CSS_SELECTOR, 'input#ap_password')

# CSS-password Re-enter input box
driver.find_element(By.CSS_SELECTOR, 'input#ap_password_check')

# CSS-continue button
driver.find_element(By.CSS_SELECTOR, 'input#continue')

# XPATH text()-conditions of use
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# XPATH text()-privacy notice
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

# CSS-signIn link - tag.class[attribute*='partial value'] format
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href*='/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F']")

# Verification

print("Test Successful")
driver.quit()
