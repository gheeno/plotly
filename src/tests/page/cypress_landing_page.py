from seleniumpagefactory.Pagefactory import PageFactory

class CypressLandingPage(PageFactory):
    '''
    Page Objects from the Cypress.io landing page.
    '''

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5

    locators = {
        '_header_testimony': ('XPATH', "//h2[contains(@class,'mb-[16px]')]"),
        '_label_weekly_downloads_amount': ('XPATH', "//div[contains(@class,'text-gray-700') and text()='Weekly downloads']/preceding-sibling::div")
    }

    ## ACTIONS ##

    def _get_string_header_testimony(self):
        return self._header_testimony.get_text()

    def _scroll_to_header_testimony(self):
        self._header_testimony.hover()

    def _get_string_weekly_download_amount(self):
        return self._label_weekly_downloads_amount.get_text()
