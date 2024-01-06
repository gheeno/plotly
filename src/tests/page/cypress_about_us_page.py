from seleniumpagefactory.Pagefactory import PageFactory


class CypressAboutUsPage(PageFactory):
    '''
    Page Objects from the Cypress.io About Us page.
    '''


    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5


    locators = {
        '_about_us_message': ('XPATH', "//p[contains(@class,'text-jade-200')]"),
        '_label_weekly_downloads_amount': ('XPATH', "//div[contains(@class,'text-gray-700') and text()='Weekly downloads']/preceding-sibling::div"),
        '_tab_company': ('ID', "dropdownCompany")
    }

    ## ACTIONS ##


    def _get_string_about_us_message(self):
        return self._about_us_message.get_text()
    
    
    def _get_current_url(self):
        return self.driver.current_url