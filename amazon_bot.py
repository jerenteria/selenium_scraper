import os
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("my_email")
password = os.getenv("password")

# path to where chrome driver is
os.environ['PATH'] += r"{{path to where chromedriver is stored}}"

# open chrome with webdriver
driver = webdriver.Chrome()
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

# find text box for email
enter_email = driver.find_element_by_id("ap_email")
# use send_keys to type in email
enter_email.send_keys(my_email)
# find enter button
email_signin = driver.find_element_by_id("continue")
# click enter button
email_signin.click()

# find box for password
enter_password = driver.find_element_by_id("ap_password")
# enter password using send_keys
enter_password.send_keys(password)
# find enter button
password_signin = driver.find_element_by_id("signInSubmit")
# click enter password button
password_signin.click()

# find sear bar
search = driver.find_element_by_id("twotabsearchtextbox")
# enter what product you want
search.send_keys("ps5 ssd")
# find enter button for product search bar
enter_search = driver.find_element_by_id("nav-search-submit-button")
# press enter
enter_search.click()

# find product that you want
ssd = driver.find_element('{{product that you want to get}}')
# click on item
select_ssd = ssd.click()