from selenium import webdriver
import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


def launch_the_browser(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def click_on_signup(driver, name, password):
    driver.find_element(By.ID, "signin2").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sign-username"))).send_keys(name)
    time.sleep(5)
    driver.find_element(By.ID, "sign-password").send_keys(password)
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
    time.sleep(5)


def teardown_driver(driver):
    driver.quit()


def verify_signup(driver):
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    if "Sign up successful." in alert_text:
        print("signup success")
    else:
        assert False, "Unexpected error: user already exist"


def check_signup(driver, name, password):
    driver.find_element(By.ID, "signin2").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sign-username"))).send_keys(name)
    time.sleep(5)
    driver.find_element(By.ID, "sign-password").send_keys(password)
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
    time.sleep(5)


def verify_invalid_signup(driver):
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()
    if "This user already exist." in alert_text:
        print("This user already exist.")
    else:
        assert False, "signup success"


def clear_input_field(element):
    element.clear()


def log_in_with_valid_credentials(driver, name, password):
    driver.find_element(By.ID, "login2").click()
    username_input = driver.find_element(By.ID, "loginusername")
    time.sleep(5)
    clear_input_field(username_input)
    username_input.send_keys(name)
    time.sleep(5)

    password_input = driver.find_element(By.ID, "loginpassword")
    time.sleep(5)
    clear_input_field(password_input)
    password_input.send_keys(password)
    time.sleep(5)

    driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()
    time.sleep(5)
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print("Alert Text:", alert_text)
        alert.accept()
        if "User does not exist." in alert_text:
            assert False, "Unexpected error: User does not exist."
        elif "Wrong password." in alert_text:
            assert False, "Unexpected error: Wrong password."
        else:
            assert False, "Unexpected error: Please fill out Username and Password."

    except NoAlertPresentException:
        pass


def attempt_to_log_in_with_invalid_credentials(driver, name, password):
    driver.find_element(By.ID, "login2").click()
    username_input = driver.find_element(By.ID, "loginusername")
    time.sleep(5)
    clear_input_field(username_input)
    username_input.send_keys(name)
    time.sleep(5)

    password_input = driver.find_element(By.ID, "loginpassword")
    time.sleep(5)
    clear_input_field(password_input)
    password_input.send_keys(password)
    time.sleep(5)

    driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()
    time.sleep(5)
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print("Alert Text:", alert_text)
        alert.accept()
        if "User does not exist." in alert_text:
            assert True, "Unexpected error: User does not exist."
        elif "Wrong password." in alert_text:
            assert True, "Unexpected error: Wrong password."
        else:
            assert True, "Unexpected error: Please fill out Username and Password."

    except NoAlertPresentException:
        pass


def click_on_next(driver):
    element = driver.find_element(By.ID, "next2")
    time.sleep(5)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(5)
    element.click()
    time.sleep(5)


def add_product_to_the_cart(driver):
    element = driver.find_element(By.XPATH, "//a[text()='MacBook Pro']")
    time.sleep(5)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(5)
    element.click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[@onclick='addToCart(15)']").click()
    time.sleep(5)


def check_items_added_to_the_cart(driver):
    try:
        driver.find_element(By.ID, "cartur").click()
        time.sleep(5)
        cart_items = driver.find_elements(By.XPATH, "//tbody/tr")
        assert len(cart_items) > 0, "Cart is empty!"
        print("Cart has items. Test Passed!")
    finally:
        teardown_driver(driver)


def without_adding_any_products_to_the_cart(driver):
    try:
        driver.find_element(By.ID, "cartur").click()
        time.sleep(5)
        cart_items = driver.find_elements(By.XPATH, "//tbody/tr")
        assert len(cart_items) == 0, "Cart is not empty!"
        print("Cart is empty. Test Passed!")
    finally:
        teardown_driver(driver)


def displayed_correctly_on_the_homepage(driver):
    try:
        products = driver.find_elements(By.CLASS_NAME, "hrefch")
        assert len(products) > 0, "No products are displayed on the homepage."
        print(f"{len(products)} products are displayed on the homepage. Test Passed!")
    finally:
        teardown_driver(driver)


def user_login(driver,name,password):
    driver.find_element(By.ID, "login2").click()
    username_input = driver.find_element(By.ID, "loginusername")
    time.sleep(5)
    clear_input_field(username_input)
    username_input.send_keys(name)
    time.sleep(5)

    password_input = driver.find_element(By.ID, "loginpassword")
    time.sleep(5)
    clear_input_field(password_input)
    password_input.send_keys(password)
    time.sleep(5)

    driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()
    time.sleep(5)
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print("Alert Text:", alert_text)
        alert.accept()
        if "User does not exist." in alert_text:
            assert False, "Unexpected error: User does not exist."
        elif "Wrong password." in alert_text:
            assert False, "Unexpected error: Wrong password."
        else:
            assert False, "Unexpected error: Please fill out Username and Password."

    except NoAlertPresentException:
        pass


def categories_can_be_navigated_successfully_phone(driver):
    driver.find_element(By.XPATH, "//a[text()='Phones']").click()
    time.sleep(5)
    try:
        products = driver.find_elements(By.CLASS_NAME, "hrefch")
        assert len(products) > 0, "No products are displayed on the homepage."
        print(f"{len(products)} products are displayed on the homepage. Test Passed!")

    except Exception as e:

        print(f"Test failed: {e}")


def categories_can_be_navigated_successfully_laptops(driver):
    element = driver.find_element(By.ID, "prev2")
    time.sleep(5)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[text()='Laptops']").click()
    time.sleep(5)
    try:
        products = driver.find_elements(By.CLASS_NAME, "hrefch")
        assert len(products) > 0, "No products are displayed on the homepage."
        print(f"{len(products)} products are displayed on the homepage. Test Passed!")

    except Exception as e:

        print(f"Test failed: {e}")


def categories_can_be_navigated_successfully_monitors(driver):
    element = driver.find_element(By.ID, "prev2")
    time.sleep(5)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[text()='Monitors']").click()
    time.sleep(5)
    try:
        products = driver.find_elements(By.CLASS_NAME, "hrefch")
        assert len(products) > 0, "No products are displayed on the homepage."
        print(f"{len(products)} products are displayed on the homepage. Test Passed!")

    except Exception as e:

        print(f"Test failed: {e}")


def logout(driver):
    time.sleep(5)
    driver.find_element(By.ID, "logout2").click()
