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
        '_button_npm_install_cypress': ('XPATH', "//span[text()='npm install cypress']"),
        '_tab_product': ('ID', "dropdownProduct"),
        '_visual_review_dropdown': ('XPATH', "(//span[text()='Visual Reviews'])[1]"),
        '_smart_orchestration_dropdown': ('XPATH', "(//span[text()='Smart Orchestration'])[1]"),
        '_pagination_swiper': ('XPATH', "(//span[contains(@class,'wiper-pagination-bullet')])[1]")
    }

    ## ACTIONS ##

    def _get_string_header_testimony(self):
        return self._header_testimony.get_text()


    def _scroll_to_header_testimony(self):
        self._header_testimony.hover()

    
    def _scroll_to_swiper(self):
        '''
        So that the _label_weekly_downloads_amount can be seen by the user.
        '''
        self._pagination_swiper.hover()


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


    def _hover_product_tab(self):
        self._tab_product.hover()
    

    def _click_visual_reviews_dropdown(self):
        self._visual_review_dropdown.click_button()


    def _click_smart_orchestration_dropdown(self):
        self._smart_orchestration_dropdown.click_button()