from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# init driver
s = Service('C:\\Users\\carte\\Automation\\python-selenium-automation\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# open the url
driver.get('https://www.amazon.com/')

# Locators - CSS & XPATH practice
# CSS-Amazon Cart
driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite').click()

# verification-verify that everything works and this opens the right webpage.
expected_result = 'Your Amazon Cart is empty'
actual_result = driver.find_element(By.XPATH, "//h2").text
assert expected_result == actual_result, f'Error! Actual test {actual_result} does not match expected result {expected_result}'

print('Test Successful')
driver.quit()
