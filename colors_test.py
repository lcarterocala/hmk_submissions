from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# init driver
s = Service('C:\\Users\\carte\\Automation\\python-selenium-automation\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.wait = WebDriverWait(driver, timeout=10)


driver.implicitly_wait(5)


# driver = webdriver.Chrome(executable_path='C:/Users/carte/Automation/python-selenium-automation/chromedriver.exe')
driver.get('https://www.amazon.com/dp/B081YS2F7N?th=1&psc=1')


# list of locators
# COLORS_LOC = (By.CSS_SELECTOR, 'div#tp-inline-twister-dim-values-container li')
# COLORS_LOC = (By.CSS_SELECTOR, 'div#inline-twister-row-color_name li')
# COLORS_LOC = (By.CSS_SELECTOR, "span[id*='color_name'] img[id*='inline']")
# COLORS_LOC = (By.CSS_SELECTOR, "div#inline-twister-row-color_name img[id*='inline-twister']")
# COLORS_LOC = (By.CSS_SELECTOR, "div#tp-inline-twister-dim-values-container img[id*='inline-twister-image']")
# COLORS_LOC = (By.CSS_SELECTOR, "#inline-twister-expander-content-color_name li[class*='a-']")
# COLORS_LOC = (By.CSS_SELECTOR, "div#inline-twister-row-color_name img[id*=inline]")
COLORS_LOC = (By.CSS_SELECTOR, "img[id*='inline-twister-image']")
COLOR_ID = (By.CSS_SELECTOR, 'inline-twister-expanded-dimension-text-color_name')


driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id*='color_name'] img[id*='inline")))
colors_locator_count = driver.find_elements(*COLORS_LOC)
# color_id = driver.find_element(*COLOR_ID)

colors = []
count = 1
print("Total Number of products:", len(colors_locator_count))
for item in range(len(colors_locator_count)):
    # color_id = driver.find_element(*COLOR_ID).text
    colors = colors_locator_count[item].text
    print(colors)



# for i in range(len(colors_locator_count)):
#    sleep(3)
#    color_name_id = colors_locator_count[i]
    # color_name_id.click()
    # color_id = driver.find_element(*COLOR_ID).text
#    print("Product", count, color_name_id)
#    count = count + 1


print("Test Successful")
driver.quit()



