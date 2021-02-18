from selenium.webdriver.common.keys import Keys
import json


class Log_In():
    
    sign_In_header = "a[title='Log in to your customer account']"
    email = "email"
    password = "passwd"
    sign_In = "SubmitLogin"

    def __init__(self, driver):
        self.driver = driver


    def test_Header_sign_In(self):
        self.driver.find_element_by_css_selector(self.sign_In_header).click()

    def test_Enter_Email_Pass_Sign_in(self):
        with open ('config.json') as f:
                data = json.load(f)
        self.driver.find_element_by_id(self.email).send_keys(['email'])
        self.driver.find_element_by_id(self.password).send_keys(['password'])
        self.driver.find_element_by_id(self.sign_In).click()