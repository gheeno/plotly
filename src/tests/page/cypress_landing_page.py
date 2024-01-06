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
        '_label_weekly_downloads_amount': ('XPATH', "//div[contains(@class,'text-gray-700') and text()='Weekly downloads']/preceding-sibling::div"),
        '_tab_company': ('ID', "dropdownCompany"),
        '_flex_about_cypress': ('XPATH', "//span[text()='About Cypress ']"),
        '_button_install': ('XPATH', "//button[text()=' Install ']"),
        '_button_npm_install_cypress': ('XPATH', "//span[text()='npm install cypress']")
    }

    ## ACTIONS ##

    def _get_string_header_testimony(self):
        return self._header_testimony.get_text()


    def _scroll_to_header_testimony(self):
        self._header_testimony.hover()


    def _get_string_weekly_download_amount(self):
        return self._label_weekly_downloads_amount.get_text()
    

    def _hover_company_tab(self):
        self._tab_company.hover()


    def _click_about_cypress_flex(self):
        self._flex_about_cypress.click_button()


    def _click_install_button(self):
        self._button_install.click_button()

    def _click_npm_install_cypress_button(self):
        self._button_npm_install_cypress.click_button()
