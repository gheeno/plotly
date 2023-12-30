from seleniumpagefactory.Pagefactory import PageFactory


class SampleApp(PageFactory):
    '''
    Page Objects from the Dash App `sample_app` under src/apps.
    '''


    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5  


    locators = {
        '_plot_dropdown': ('ID', "react-select-2--value"),
        '_plot_dropdown_scatter_plot': ('XPATH', "//div[contains(@class, 'VirtualizedSelectOption') and text()= 'Scatter Plot']"),
        '_plot_dropdown_bar_plot': ('XPATH', "//div[contains(@class, 'VirtualizedSelectOption') and text()= 'Bar Plot']"),
        '_plot_svg_scatter_canvas_top_point': ('XPATH', "(//*[name()='svg']//*[name()='g']//*[name()='path' and @class='point' and contains(@style, 'rgb(99, 110, 250)')])[1]"),
        '_plot_svg_scatter_canvas_top_point_val': ('XPATH', "//*[name()='svg']//*[name()='g']//*[name()='text' and @class='nums']")
    }


    def _click_dropdown(self):
        self._plot_dropdown.click()


    def _click_dropdown_option(self, option):
        if option == 'Bar Plot':
            self._plot_dropdown_bar_plot.click()
        else:
            self._plot_dropdown_scatter_plot.click()

    
    def _hover_over_top_scatter_point(self):
        self._plot_svg_scatter_canvas_top_point.hover()

    
    def _get_attribute_top_scatter_point_value(self):
        return self._plot_svg_scatter_canvas_top_point_val.getAttribute("data-unformatted")

