# webdriver is what allows to interact with web
from selenium import webdriver

PATH = "/Users/Juan_1/Desktop/chromedriver"

# the driver we are using is google chrome
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")