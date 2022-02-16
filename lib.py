from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import sys

class LIB:

    def __init__(self):
        self.config_data = self.load_config()
        self.test_data = self.load_test_data()


    def load_config(self):
            with open ('config.json') as f:
                data = json.load(f)
            return data

    def load_test_data(self):
        with open ('test_data.json') as f:
            test_data = json.load(f)
        return test_data

    #create Chrome driver
    def open_browser(self):
        try:
            browser = webdriver.Chrome()
            browser.maximize_window()
            return browser
        except:
            print('Something went wrong during browser opening')

    #navigate to given url-page
    def page_load(self, browser):
        try:
            browser.get(self.config_data['url'])
        except:
            print('Something went wrong with page loading')

    #open txt file
    def write_to_file(self, text):
        try:
            with open("log.txt", "a") as f:
                return file.write("\n" + str(text))
        except:
            print("Error during writing to file!")

    #move to given element
    def move_to_element(self, browser, element):
        try:
            action = ActionChains(browser)
            action.move_to_element(element).perform()
        except:
            print("Can not move to given element!")

    #wait for given element to be visible in UI
    def wait_for_element(self, browser, element):
        try:
            WebDriverWait(browser, 30).until(EC.visibility_of_element_located(element))
        except:
            print("Element is not visible!")

    #wait for given elements to be visible in UI
    def wait_for_elements(self, browser, elements):
        try:
            WebDriverWait(browser, 30).until(EC.visibility_of_any_elements_located(element))
        except:
            print("Elements are not visible!")

    #get data
    def get_data(self, key):
        try:
            with open('test_data.json') as f:
                data = json.load(f)
            return data[key]
        except:
            print("Error during data getting!")

    # get data from config file
    def get_config_data(self, key):
        try:
            with open('config.json') as f:
                data = json.load(f)
            return data[key]
        except:
            print("Error during data getting!")


    #save screenshot
    def save_screenshot(self, browser):
        current_filename = os.path.basename(sys.argv[0][:-3])
        try:
            browser.save_screenshot(f'Test\\{current_filename}_screenshot.png')
        except:
            print('Screenshot is not saved!')

    #close browser
    def close_browser(self, browser):
        try:
            browser.quit()
        except:
            ('Something went wrong with closing browser')


























