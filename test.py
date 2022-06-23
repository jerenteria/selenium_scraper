import os
from selenium import webdriver

os.environ['PATH'] += r"C:/Users/Juan_1/Desktop/Projects/selenium_chrome_driver"
# driver is what actually lets selenium navigate the page
# the driver is using chrome
driver = webdriver.Chrome()
driver.get("https://shop.warriors.com/mens-new-era-white/black-golden-state-warriors-2022-nba-finals-champion-locker-room-9fifty-snapback-adjustable-hat/p-48199842529623+z-9334-1782012830?_ref=p-TLP:m-GRID:i-r0c1:po-1?utm_source=website&utm_medium=championshippage&utm_campaign=champhats-20220616")

# hat = driver.find_element_by_class_name("Gear-item-image")
# search_button = driver.find_element_by_name("btnK")
add_hat_to_cart = driver.find_element_by_class_name("button large primary")

driver.implicitly_wait(10)
# search_box.send_keys("PS5")


