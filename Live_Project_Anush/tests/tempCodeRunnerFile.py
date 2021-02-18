import json
from pages.contact_us import Contact_Us
from lib import LIB

def test_contact_us():
    try:
        open_page = LIB()
        browser = open_page.open_browser()
        open_page.page_load(browser)
        subject_heading = open_page.test_data['subject_heading'][1]
        message = open_page.test_data['message']
        image = open_page.test_data['img_path']
        order_refferance = open_page.test_data['ord_refferance']
        email_address = open_page.config_data['email']


        send_message = Contact_Us(browser)

        #select subject heading
        send_message.select_subject_heading('subject_heading')

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



test_contact_us()