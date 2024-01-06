from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from PIL import Image, ImageChops, ImageStat
from io import BytesIO
import glob
import os 


input_test_analytics_image = './src/images/input/expected_test_analytics_green.png'
output_test_analytics_image = './src/images/output/actual_test_analytics_green.png'
comparison_test_analytics_image = './src/images/output/comparison_test_analytics_green.png'


class CypressCloudOptions(PageFactory):
    '''
    Page Objects from the Cypress cloud tab options.
    '''


    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5


    locators = {
        '_test_analytics_option': ('XPATH', "//a[text() = 'Test Analytics']")
    }

    ## ACTIONS ##


    def _hover_test_analytics_option(self):
        return self._test_analytics_option.hover()
    

    def _clear_output_results(self):
        files = glob.glob('./src/images/output/*')
        for f in files:
            os.remove(f)


    def _img_capture_test_analytics_option(self):
        with open(output_test_analytics_image, 'wb') as file:
            file.write(self.driver.find_element(By.XPATH, "//a[text() = 'Test Analytics']").screenshot_as_png)

    
    def _compare_image_and_get_difference(self):
        expected_image = Image.open(input_test_analytics_image)
        actual_image = Image.open(output_test_analytics_image)
        result = ImageChops.difference(expected_image, actual_image)
        stat = ImageStat.Stat(result)
        diff_val = sum(stat.mean)
        return diff_val
