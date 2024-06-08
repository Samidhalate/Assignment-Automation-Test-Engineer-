*** Settings ***
Library  SeleniumLibrary
Variables    ../Environment/QA/app_config.yaml
Library     ../Library/web_auto.py
Library    Screenshot
Library    Process


*** Variables ***
${driver}    launch_the_browser

*** Keywords ***
User_SignUp_with_valid_details
    ${driver}    launch_the_browser    ${app_config.url}
    click_on_signup      ${driver}     ${Signup.name}    ${Signup.password}
    verify_signup        ${driver}     

User_SignUp_with_Invalid_details
    ${driver}    launch_the_browser    ${app_config.url}
    check_signup      ${driver}        ${Signup.name1}    ${Signup.password2}
    verify_invalid_signup       ${driver}

Positive_scenario_User_login_with_valid_credentials
    ${driver}    launch_the_browser    ${app_config.url}
    log_in_with_valid_credentials    ${driver}     ${Login.name}    ${Login.password}

Negative_scenario_Attempt_to_login_with_invalid_credentials
    ${driver}    launch_the_browser    ${app_config.url}
    attempt_to_log_in_with_invalid_credentials    ${driver}    ${Login.name1}    ${Login.password2}

Successfully_log_out
    ${driver}    launch_the_browser    ${app_config.url}
    user_login    ${driver}    ${Login.name}    ${Login.password}
    logout    ${driver}

Navigate_to_the_last_page_select_the_last_product_and_add_the_product_to_the_cart
    ${driver}    launch_the_browser    ${app_config.url}
    user_login    ${driver}    ${Login.name}    ${Login.password}
    click_on_next    ${driver}
    add_product_to_the_cart    ${driver}

Successfully_check_the_items_added_to_the_cart
    ${driver}    launch_the_browser    ${app_config.url}
    user_login    ${driver}    ${Login.name}    ${Login.password}
    check_items_added_to_the_cart    ${driver}
    
    
checkout_without_adding_any_products_to_the_cart 
    ${driver}    launch_the_browser    ${app_config.url}
    user_login    ${driver}      ${Login.name}    ${Login.password}
    without_adding_any_products_to_the_cart    ${driver}
    
Verify_that_products_are_displayed_correctly_on_the_homepage
    ${driver}    launch_the_browser    ${app_config.url}
    user_login    ${driver}    ${Login.name}    ${Login.password}
    displayed_correctly_on_the_homepage    ${driver}
    
    
Verify_that_product_categories_can_be_navigated_successfully 
     ${driver}    launch_the_browser    ${app_config.url}
     user_login    ${driver}    ${Login.name}    ${Login.password}
     categories_can_be_navigated_successfully_phone    ${driver}
     categories_can_be_navigated_successfully_laptops    ${driver}
     categories_can_be_navigated_successfully_monitors    ${driver}