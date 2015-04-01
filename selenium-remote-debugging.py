from selenium.webdriver import ChromeOptions, Remote
from selenium import webdriver


options = ChromeOptions()
options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')

driver = Remote(command_executor='http://127.0.0.1:9515', desired_capabilities=options.to_capabilities())
driver.get("http://www.wikipedia.org")
