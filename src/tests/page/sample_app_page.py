from seleniumpagefactory.Pagefactory import PageFactory
import pdb


class SampleApp(PageFactory):
    '''
    Page Objects from the Dash App `sample_app` under src/apps.
    '''


    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5  


    locators = {
        '_plot_dropdown': ('ID', "react-select-2--value"),
        '_plot_dropdown_option': ('XPATH', "//div[contains(@class, 'VirtualizedSelectOption')]")
    }


    def _click_dropdown(self):
        self._plot_dropdown.click()


    def _click_dropdown_option(self, option):
        self._plot_dropdown_option.select_element_by_value(option)