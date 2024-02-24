from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when("Switch to the newly opened window")
def switch_to_new_window(context):
    context.app.terms_and_conditions.switch_to_new_window()


@then("Verify Terms and Conditions page is opened")
def terms_and_conditions_open(context):
    context.app.terms_and_conditions.terms_and_conditions_open()


@then("User can close new window")
def user_can_close_window(context):
    context.driver.close()


@then("switch back to original window")
def switch_to_original_window(context):
    context.app.terms_and_conditions.switch_to_window_by_id(context.original_windows)
