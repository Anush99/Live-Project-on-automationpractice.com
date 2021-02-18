'''
Scenario
1. Go to URL
2. Click to Sign In in home page
3. Fill email address and password
4. Click Sign In button
5. Verify that you signed successfully

'''
import pytest
import json
from pages.sign_in_page import Log_In
from pages.home_page_logged_in import Home_Page
from lib import LIB


def test_sign_in():
    try:
        #open browser
        open_page = LIB()
        browser = open_page.open_browser()

        #open url
        open_page.page_load(browser)

        sign_in = Log_In(browser)

        # click on Sign In button in header
        browser.find_element_by_css_selector(sign_in.sign_In_header).click()

        #wait for email field visibility
        open_page.wait_for_element(browser, sign_in.sign_In)

        # enter email address
        sign_in.enter_email()

        # enter password
        sign_in.enter_password()

        #click Sign In button
        sign_in.click_sign_in()

        #verify Sign in
        home_page = Home_Page(browser)
        
        registered_name = home_page.get_account_Sign_In_Name()
        config_registered_name = open_page.config_data['registered_name']
        assert registered_name == config_registered_name, open_page.save_screenshot(browser)
        


    finally:
        #close browser
        open_page.close_browser(browser)

