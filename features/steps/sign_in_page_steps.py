from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when("Input email and password")
def user_user_name(context):
    context.app.sign_in_page.user_user_name()
    context.app.sign_in_page.password()
    context.app.sign_in_page.sign_in_button()


@when("Store original windows")
def store_original_windows(context):
    context.original_windows = context.driver.current_window_handle


@when("Click on Target terms and conditions link")
def click_on_target_terms_and_conditions(context):
    context.app.sign_in_page.click_on_target_terms_and_conditions()