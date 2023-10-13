from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create a new instance of the Google Chrome driver
driver = webdriver.Chrome()

# Go to the Google home page
driver.get("https://www.google.com")
print("Opened Google")

# Open a new tab
driver.execute_script("window.open('');")
time.sleep(1)

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])
print("Opened a new tab")

# Navigate to a different website
driver.get("https://www.wikipedia.org/")
print("Navigated to Wikipedia")

# Wait for 5 seconds
time.sleep(5)

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print("Scrolled to the bottom of the page")
time.sleep(3)

# Scroll back to the top of the page
driver.execute_script("window.scrollTo(0, 0);")
print("Scrolled back to the top of the page")

# Close the new tab
driver.close()
print("Closed the new tab")

# Switch back to the original tab
driver.switch_to.window(driver.window_handles[0])
print("Switched back to the original tab")

# Capture a screenshot of the search results
driver.save_screenshot("search_results.png")
print("Captured a screenshot of the search results (search_results.png)")

# Close the browser
driver.quit()
print("Closed the browser")
