from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# Connect to ChromeDriver (error, code deprecated)
# driver = webdriver.Chrome(executable_path='C:/Users/carte/Automation/python-selenium-automation/chromedriver.exe')
s = Service('C:\\Users\\carte\\Automation\\python-selenium-automation\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Access & Connect to amazon's customer service page
driver.get('https://www.amazon.com/gp/help/customer/display.html')

# Locator build for help library search field - cancel order entered
search = driver.find_element(By.XPATH, "//input[@id='helpsearch']")
search.clear()
search.send_keys('cancel order')
search.send_keys(Keys.RETURN)

# verify you are on the right page & results are correct
expected_result = 'Cancel Items or Orders'
actual_result = driver.find_element(By.XPATH, "//div[@class='help-content']//h1[text()='Cancel Items or Orders']").text
assert expected_result == actual_result, f'Error! Actual test {actual_result} does not match expected result {expected_result}'

sleep(3)
print('Test Successful')
driver.quit()


