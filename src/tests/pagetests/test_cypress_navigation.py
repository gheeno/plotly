# • User is able to click on “Product” and then “visual review”

# Bonus:
# ● User is able to click on “Product”, then “Smart Orchestration”, then scroll down to
# “Test Analytics” and see that the green circle is around “Test Analytics”

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(
  os.path.dirname(__file__), '..')))

from page.cypress_landing_page import CypressLandingPage
from page.cypress_about_us_page import CypressAboutUsPage
from page.cypress_visual_reviews_page import CypressVisualReviewsPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import time
import pyperclip


class CypressLandingPageTest():
    

    def setup(self):
        load_dotenv(dotenv_path=".env.url")
        landing_page_url = os.getenv('CYPRESS_LANDING_PAGE')

        service = Service()
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get(landing_page_url)


    def assert_weekly_downloads_value(self):
        '''
        • Users are able to visit the website and able to scroll down to “Loved by OSS,
          trusted by Enterprise” and see the weekly downloads number. 
        '''
        clp = CypressLandingPage(self.driver)
        try:
            clp._scroll_to_header_testimony()
            assert clp._get_string_header_testimony() == "Loved by OSS, trusted by Enterprise"
            assert clp._get_string_weekly_download_amount() == "5M+"
        except Exception as e:
            print(f"An error occurred: {e}")
            raise


    def assert_about_cypress_is_present(self):
        '''
        • User is able to click on Company and then on “About Cypress”
        '''
        clp = CypressLandingPage(self.driver)
        cau = CypressAboutUsPage(self.driver)
        try:
            clp._hover_company_tab()
            clp._click_about_cypress_flex()
            assert cau._get_current_url() == "https://www.cypress.io/about-us"
            assert cau._get_string_about_us_message() == "Cypress testing tools support developers all around the world by making it easier to build and test applications."
        except Exception as e:
            print(f"An error occurred: {e}")
            raise


    def assert_npm_install_is_copied(self):
        '''
        • User is able to click on “Install” and then on “npm install cypress” and make sure
          the copied text is “npm install cypress --save-dev”
        '''
        clp = CypressLandingPage(self.driver)
        try:
            clp._click_install_button()
            clp._click_npm_install_cypress_button()
            time.sleep(1) # wait for OS to copy the string.
            copied_string = pyperclip.paste()
            assert copied_string == "npm install cypress --save-dev"
        except Exception as e:
            print(f"An error occurred: {e}")
            raise


    def assert_product_visual_reviews_loads(self):
        '''
         • User is able to click on “Product” and then “visual review”
        '''
        clp = CypressLandingPage(self.driver)
        cvr = CypressVisualReviewsPage(self.driver)
        try:
            clp._hover_product_tab() # clicking the product tab doesn't "show" the visual review on the next page, we have to hover.
            clp._click_visual_reviews_dropdown()
            visual_review_url = cvr._get_current_url()
            assert visual_review_url == "https://www.cypress.io/cloud?v=2#visual_reviews"
            assert cvr._check_http_response_code(visual_review_url) == 200
            
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
        

    def teardown(self):
        self.driver.close()


### ROBOTFRAMEWORK / PYTEST ###
def test_assert_weekly_downloads():
    clpt = CypressLandingPageTest()
    clpt.setup()
    clpt.assert_weekly_downloads_value()
    clpt.teardown()


def test_assert_about_cypress_is_present():
    clpt = CypressLandingPageTest()
    clpt.setup()
    clpt.assert_about_cypress_is_present()
    clpt.teardown()


def test_assert_npm_install_command_is_copied():
    clpt = CypressLandingPageTest()
    clpt.setup()
    clpt.assert_npm_install_is_copied()
    clpt.teardown()


def test_assert_product_visual_reviews_loads():
    clpt = CypressLandingPageTest()
    clpt.setup()
    clpt.assert_product_visual_reviews_loads()
    clpt.teardown()