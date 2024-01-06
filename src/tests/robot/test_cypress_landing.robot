*** Settings ***
Library           ../pagetests/test_cypress_landing_page.py

*** Variables ***

*** Test Cases ***
As a user, I would like to scroll down to the header and see the weekly downloads amount.
    Assert weekly downloads string and header string

*** Keywords ***
Assert weekly downloads string and header string
    test_cypress_landing_page.test_assert_weekly_downloads