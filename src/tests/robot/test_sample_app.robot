*** Settings ***
Library           ../pagetests/test_sample_app.py

*** Variables ***
${MESSAGE}

*** Test Cases ***
My Test
    Run Test

*** Keywords ***
Run Test
    test_sample_app.test_sample_app_dropdown