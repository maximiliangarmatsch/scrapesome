import time
import sys

from selenium import webdriver
from insta_scrape import (
    handle_cookie_banner,
    login,
    close_saving_login_modal,
    close_notification_modal,
    open_follower_modal
)

COOKIES_ALLOWED = 1

if len(sys.argv) < 3:
    print('Argument error.')
    sys.exit()

# Passed Arguments
login_username = sys.argv[1]
login_password = sys.argv[2]

# Init driver
driver = webdriver.Firefox()
# Open Instagram
driver.get('https://www.instagram.com/')
# Handles cookies through pop-modal and value set in COOKIES_ALLOWED
handle_cookie_banner(driver, COOKIES_ALLOWED)
# Paste credentials into login form and submit
login(driver, login_username, login_password)
# Close modal for saving login cred.
close_saving_login_modal(driver)
# Close modal asking for notofications
close_notification_modal(driver)
# Visit user site
driver.get('https://www.instagram.com/berghain_ostgut/')
# Open follower modal
open_follower_modal(driver)

# inspecting time
time.sleep(500)
driver.quit()


