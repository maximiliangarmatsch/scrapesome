from selenium.webdriver.common.by import By
import time

waiting_seconds = 4


def handle_cookiebanner(driver, allow_cookies=1):
    print('handle cookie banner..')
    time.sleep(waiting_seconds)
    button_class = '_a9--'
    allow_cookies_button_class = '_a9_0'
    decline_cookies_button_class = '_a9_1'
    if allow_cookies:
        button_selector = 'button.' + button_class + '.' + allow_cookies_button_class
    else:
        button_selector = 'button.' + button_class + '.' + decline_cookies_button_class
    button = driver.find_element(By.CSS_SELECTOR, button_selector)
    button.click()
    pass


def login(driver, username, password):
    print('login with user: ' + username + '..')
    time.sleep(waiting_seconds)
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    submit_login = driver.find_element(By.CSS_SELECTOR, 'button._acan._acap._acas._aj1-')
    username_input.send_keys(username)
    password_input.send_keys(password)
    submit_login.click()


def close_saving_login_modal(driver):
    print('Close saving login info modal..')
    time.sleep(20)
    not_now_button = driver.find_element(By.CSS_SELECTOR, '._ac8f')
    not_now_button.click()


def close_notification_modal(driver):
    print('Close notification on/off modal..')
    time.sleep(20)
    not_now_button = driver.find_element(By.CSS_SELECTOR, '._a9--._a9_1')
    not_now_button.click()


def open_follower_modal(driver):
    print('Open Follower Modal..')
    time.sleep(20)
    not_now_button = driver.find_element(By.CSS_SELECTOR, 'li.xl565be.x1m39q7l.x1uw6ca5.x2pgyrj a')
    not_now_button.click()


def scroll_follower_modal(driver):
    pass


# best would be id's, anmes are okay also
def get_follower(driver):
    pass


# user id is berghain_ostgut from https://www.instagram.com/berghain_ostgut/
def get_user_info(driver, user_id):
    # num follower
    # num following
    # bio
    # (images, stories, videos) ?
    # many more.
    return
