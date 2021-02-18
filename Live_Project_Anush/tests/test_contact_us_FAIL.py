'''
1. Go to URL
2. Click to Contact US button
4. Fill all fields besides Message field in Contact US 
5. click on Send button
6. Validate that Validate message displays
7. Close browser

'''

import pytest
import json
from pages.contact_us import Contact_Us
from lib import LIB

def test_contact_us():
    try:
        open_page = LIB()
        browser = open_page.open_browser()
        open_page.page_load(browser)
        send_message = Contact_Us(browser)
        
        #click on Contact US
        browser.find_element_by_css_selector(send_message.header_contact_us).click()

        #select subject heading
        send_message.select_subject_heading(browser)

        #write email address
        send_message.email_address()

        # write order refferance
        send_message.order_refference()

        #attach file
        send_message.attach_file()

        #tap on message field
        send_message.fail_write_message()

        #send message
        send_message.send_message()

        #validation
        fail_message = 'error'
        validation = send_message.check_fail(fail_message)

        assert fail_message in validation, open_page.save_screenshot(browser)

    finally:
        #close browser
        open_page.close_browser(browser)


