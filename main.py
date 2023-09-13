import time
import sys

from selenium import webdriver
from insta_scrape import (
    handle_cookiebanner,
    login,
    close_saving_login_modal,
    close_notification_modal,
    open_follower_modal
)

if len(sys.argv) < 3:
    print('Argument error.')
    sys.exit()

allow_cookies = 1
login_username = sys.argv[1]
login_password = sys.argv[2]

driver = webdriver.Firefox()

driver.get('https://www.instagram.com/')

handle_cookiebanner(driver)
login(driver, login_username, login_password)
close_saving_login_modal(driver)
close_notification_modal(driver)

driver.get('https://www.instagram.com/berghain_ostgut/')
open_follower_modal(driver)

# inspecting time
time.sleep(500)

driver.quit()


