from selenium import webdriver
import time

# Set up the Selenium webdriver
driver = webdriver.Chrome()  # You need to have chromedriver installed and in your PATH
driver.get("https://ca.shein.com/")

# Wait for the page to load
time.sleep(8)

# Test 1: Click on the logo to ensure it redirects to the homepage
logo = driver.find_element("xpath",'//*[@id="header_logo_icon"]')
logo.click()
time.sleep(2)  # Wait for the page to load

# Test 2: Click on the "New In" link to ensure it redirects to the new arrivals page
new_in_link = driver.find_element("xpath","/html/body/div[1]/header/div[3]/div[1]/div/div[3]/nav/div[2]/div/a[1]")
new_in_link.click()
time.sleep(2)  # Wait for the page to load

# Test 3: Click on one of the navigation links to ensure it redirects to the correct page
navigation_link = driver.find_element("xpath","/html/body/div[1]/header/div[3]/div[1]/div/div[3]/nav/div[2]/div/a[8]")
navigation_link.click()
time.sleep(2)  # Wait for the page to load

# Test 4: Click on the "Sign In" button to ensure it redirects to the sign-in page
sign_in_button = driver.find_element("xpath","/html/body/div[1]/header/div[3]/div[1]/div/div[2]/div[3]/div[1]/a/i")
sign_in_button.click()
time.sleep(2)  # Wait for the page to load

# Test 5: Click on a product category link to ensure it redirects to the correct page
product_category_link = driver.find_element("xpath", "/html/body/div[1]/header/div[3]/div[1]/div/div[3]/nav/div[1]")
product_category_link.click()
time.sleep(2)  # Wait for the page to load


# Close the browser
driver.quit()
