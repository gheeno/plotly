import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(
  os.path.dirname(__file__), '..')))

from page.sample_app_page import SampleApp
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class SampleAppTests():

    def setup(self):
        service = Service()
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get("http://127.0.0.1:7685")

    def test_sample_app_dropdown_selector(self):
        '''
        As a user I would like to see if the dropdown for the Dash `Sample App` 
        can be selected.
        '''
        sa = SampleApp(self.driver)
        try:
            sa._click_dropdown()
            sa._click_dropdown_option("Scatter Plot")
            sa._hover_over_top_scatter_point()
            assert sa._get_attribute_top_scatter_point_value() == "medal=gold<br>nation=South Korea<br>count=24"
        except Exception as e:
            print(f"An error occurred: {e}")
            raise

    def teardown(self):
        self.driver.close()

### ROBOT FRAMEWORK / PYTEST ###
def test_sample_app_dropdown():
    sat = SampleAppTests()
    sat.setup()
    sat.test_sample_app_dropdown_selector()
    sat.teardown()