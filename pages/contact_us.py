from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
from lib import LIB


class Contact_Us:

    # locators
    header_contact_us = "[title='Contact Us']"
    subject_heading_locator = (By.XPATH, '//*[@name="id_contact"]')
    subject_heading = '//*[@name="id_contact"]'
    email = 'email'
    order_refference_locator = 'id_order'
    upload = 'fileUpload'
    message = 'message'
    submit_message = 'submitMessage'
    success_message = "p[class='alert alert-success']"
    error_message = "div[class='alert alert-danger']"

    def __init__(self, browser):
        self.browser = browser

    
    def select_subject_heading(self, browser):
        LIB.wait_for_element(self, browser, self.subject_heading_locator)
        select_text = LIB.get_data(self, key = 'subject_heading')
        select = Select(self.browser.find_element_by_xpath(self.subject_heading))
        select.select_by_visible_text(select_text)

    def email_address(self):
        email = LIB.get_config_data(self, key = 'email')
        self.browser.find_element_by_id(self.email).send_keys(email)

    def order_refference(self):
        order_ref = LIB.get_data(self, key = 'ord_refferance')
        self.browser.find_element_by_id(self.order_refference_locator).send_keys(order_ref)
  

    def attach_file(self):
        img = LIB.get_data(self, key = 'img_path')
        self.browser.find_element_by_id('fileUpload').send_keys(img)


    def write_message(self):
        message = LIB.get_data(self, key = 'message')
        self.browser.find_element_by_id(self.message).send_keys(message)

    def fail_write_message(self):
        self.browser.find_element_by_id(self.message).click()

    def send_message(self):
        self.browser.find_element_by_id(self.submit_message).click()

    def check_success(self, text):
        elem = self.browser.find_element_by_css_selector(self.success_message)
        text = elem.text
        return text

    def check_fail(self, text):
        elem = self.browser.find_element_by_css_selector(self.error_message)
        text = elem.text
        return text


    