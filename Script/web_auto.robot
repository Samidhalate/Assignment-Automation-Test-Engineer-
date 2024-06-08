*** Settings ***
Library  SeleniumLibrary
Resource  ../Keyword/web_auto_Keyword..robot

*** Test Cases ***
User SignUp:Signup with valid details
      [Tags]     e-commerce    signup
      User_SignUp_with_valid_details

User SignUp:Signup with Invalid details
      [Tags]    e-commerce    signup2
      User_SignUp_with_Invalid_details


User login:Signup with valid details
      [Tags]    e-commerce    login1
      Positive_scenario_User_login_with_valid_credentials

User login:Signup with invalid credentials
      [Tags]    e-commerce    login2
      Negative_scenario_Attempt_to_login_with_invalid_credentials

Attempt to checkout without adding any products to the cart
    [Tags]    e-commerce    empty
    checkout_without_adding_any_products_to_the_cart

Adding products to the shopping cart
      [Tags]    e-commerce    cart
      Navigate_to_the_last_page_select_the_last_product_and_add_the_product_to_the_cart

Checkout process
     [Tags]    e-commerce    check
     Successfully_check_the_items_added_to_the_cart


Verify that products are displayed
    [Tags]    e-commerce    display
    Verify_that_products_are_displayed_correctly_on_the_homepage

Verify that product categories can be navigated successfully
    [Tags]    e-commerce    navigate
    Verify_that_product_categories_can_be_navigated_successfully

Logout process 
      [Tags]    e-commerce    logout
      Successfully_log_out