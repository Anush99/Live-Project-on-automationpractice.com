'''
1. Go to Contact us button
3. Fill all fields in Contact us and click on Send button
4.Validate that success message displays
5. Close browser
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

        #write message
        send_message.write_message()

        #send message
        send_message.send_message()

        #validation
        success_message = 'successfully sent'
        validation = send_message.check_success(success_message)

        assert success_message in validation, open_page.save_screenshot(browser)
 
    finally:
        #close browser
        open_page.close_browser(browser)


