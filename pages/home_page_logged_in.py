from lib import LIB

class Home_Page:
    
    # locators
    
    sign_out = "logout"
    account_Sign_In_name = "[title='View my customer account']"
    order_history_and_details = "[title='Orders']"
    my_credit_slips = "[title='Credit slips']"
    my_addresses = "[title='Addresses']"
    my_personal_info = "[title='Information']"


    def __init__(self, driver):
        self.driver = driver

    def click_on_Sign_Out(self):
        self.driver.find_element_by_class_name(self.sign_out).click()

    def get_account_Sign_In_Name(self):
        text = self.driver.find_element_by_css_selector(self.account_Sign_In_name).text
        return text

    def open_order_history_and_details(self):
        self.driver.find_element_by_css_selector(self.order_history_and_details).click()
    
    def my_credit_slips(self):
        self.driver.find_element_by_css_selector(self.my_credit_slips).click()

    def my_addresses(self):
        self.driver.find_element_by_css_selector(self.my_addresses).click()

    def my_personal_info(self):
        self.driver.find_element_by_css_selector(self.my_personal_info).click()