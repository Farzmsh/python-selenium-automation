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

# @then("Input email and password on SignIn page")

