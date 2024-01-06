from seleniumpagefactory.Pagefactory import PageFactory
import requests
import logging


class CypressVisualReviewsPage(PageFactory):
    '''
    Page Objects from the Cypress.io Visual Reviews page.
    '''


    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5


    locators = {}

    ## ACTIONS ##


    def _get_current_url(self):
        return self.driver.current_url
    

    def _check_http_response_code(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.status_code
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to make an HTTP request: {e}")
            return None