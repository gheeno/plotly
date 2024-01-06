# • User is able to click on Company and then on “About Cypress”

# • User is able to click on “Install” and then on “npm install cypress” and make sure
# the copied text is “npm install cypress --save-dev”

# • User is able to click on “Product” and then “visual review”

# Bonus:
# ● User is able to click on “Product”, then “Smart Orchestration”, then scroll down to
# “Test Analytics” and see that the green circle is around “Test Analytics”

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(
  os.path.dirname(__file__), '..')))

from page.cypress_landing_page import CypressLandingPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv


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
        
    def teardown(self):
        self.driver.close()

### PYTEST ###
def test_assert_weekly_downloads():
    clpt = CypressLandingPageTest()
    clpt.setup()
    clpt.assert_weekly_downloads_value()
    clpt.teardown()