from selenium.webdriver.common.keys import Keys
import json
from lib import LIB


class Log_In():
    
    # locators
    sign_In_header = "a[title='Log in to your customer account']"
    email = "email"
    password = "passwd"
    sign_In = "SubmitLogin"

    def __init__(self, browser):
        self.browser = browser

    # enter email address
    def enter_email(self):
        email = LIB.get_config_data(self, key = 'email')
        self.browser.find_element_by_id(self.email).send_keys(email)
    
    # enter password
    def enter_password(self):
        password = LIB.get_config_data(self, key = 'password')
        self.browser.find_element_by_id(self.password).send_keys(password)

    # click on Sign in button
    def click_sign_in(self):
        self.browser.find_element_by_id(self.sign_In).click()