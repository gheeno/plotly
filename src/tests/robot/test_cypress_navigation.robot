*** Settings ***
Library           ../pagetests/test_cypress_navigation.py

*** Variables ***


*** Test Cases ***
As a user, I would like to scroll down to the header and see the weekly downloads amount.
    Assert weekly downloads string and header string


As a user, I would like to visit the About Cypress page via the Company Tab and About Cypress label.
    Assert ABOUT CYPRESS page by using hover and click


As a user, I would like to see if the NPM INSTALL CYPRESS button actually copies the proper command.
    Assert that npm install cypress install button copies the right command


As a user, I would like if the Visual Reviews page loads from the Product Option.
    Assert that Product / Visual Reviews is accessible and loads properly


As a user, if I hover over the Test Analytics option from the Cloud toolbar, I should see a green ring around it.
    Assert Test Analytics has a green circle around it

*** Keywords ***
Assert weekly downloads string and header string
    test_cypress_navigation.test_assert_weekly_downloads


Assert ABOUT CYPRESS page by using hover and click
    test_cypress_navigation.test_assert_about_cypress_is_present


Assert that npm install cypress install button copies the right command
    test_cypress_navigation.test_assert_npm_install_command_is_copied


Assert that Product / Visual Reviews is accessible and loads properly
    test_cypress_navigation.test_assert_product_visual_reviews_loads


Assert Test Analytics has a green circle around it
    test_cypress_navigation.test_assert_green_circle_around_test_analytics