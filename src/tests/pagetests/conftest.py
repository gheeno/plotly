import time
import os
from datetime import datetime    
import pytest
from selenium import webdriver as selenium_webdriver
from selenium.webdriver.chrome.options import Options

# set up webdriver fixture
@pytest.fixture(scope='session')
def selenium_driver(request):
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')

    driver = selenium_webdriver.Chrome(options=chrome_options)
    # driver.set_window_size(1920, 1080)
    # driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    driver.quit()


# set up a hook to be able to check if a test has failed
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        feature_request = item.funcargs['request']
        driver = feature_request.getfixturevalue('selenium_driver')
        nodeid = item.nodeid
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H_%M")}.png'.replace("/", "_").replace("::", "_").replace(".py", "")
            img_path = os.path.join("screenshots", file_name)
            driver.save_screenshot(img_path)
            screenshot = driver.get_screenshot_as_base64()
            extra.append(pytest_html.extras.image(screenshot, ''))
        report.extras = extra


# check if a test has failed
@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs['selenium_driver']
            take_screenshot(driver, request.node.nodeid)
            print("executing test failed", request.node.nodeid)


# make a screenshot with a name of the test, date and time
def take_screenshot(driver, nodeid):
    time.sleep(1)
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/","_").replace("::","__")
    driver.save_screenshot(os.path.join("screenshots", file_name))
