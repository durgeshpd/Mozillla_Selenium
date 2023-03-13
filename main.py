from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Specify the path to the Firefox executable
firefox_path = "/usr/bin/firefox"

# Automatically download and install the appropriate geckodriver
gecko_service = Service(executable_path=GeckoDriverManager().install())

# Create a new instance of the Firefox browser using the geckodriver and Firefox executable
options = webdriver.FirefoxOptions()
options.binary_location = firefox_path
driver = webdriver.Firefox(service=gecko_service, options=options)

# Use Firefox to navigate to a URL
driver.get('https://www.google.com')

# Close the browser
driver.quit()
