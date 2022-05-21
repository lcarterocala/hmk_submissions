from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Connect to ChromeDriver
driver = webdriver.Chrome(executable_path='C:/Users/carte/Automation/python-selenium-automation/chromedriver.exe')
# Connect to amazon's sign-in page
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

# Locator build for Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Locator build for the Continue Button
driver.find_element(By.XPATH, "//input[@id='continue']")

# Locator build for the need help link - use .click() to access child links
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Locator build for the Forgot your password link
# using multiple elements - parent/child relationship
driver.find_element(By.XPATH, "//div[@class='a-section']//a[@id='auth-fpp-link-bottom']")

# Locator build for Other issues with Sign-in Link
driver.find_element(By.XPATH, "//div[@class='a-section']//a[@id='ap-other-signin-issues-link']")

# Locator build for Create your Amazon account - button
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")

# Locator build for Conditions of use
# using multiple elements - parent/child relationship
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Conditions of Use']")

# Locator build for Privacy Notice
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Privacy Notice']")


sleep(2)
print('Test Successful')
driver.quit()