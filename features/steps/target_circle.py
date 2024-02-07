from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CIRCLE_LINK = (By.XPATH, "(//a[@data-test='@web/GlobalHeader/UtilityHeader/TargetCircle'])")


@when('open target circle page')
def step_impl(context):
    context.driver.find_element(*CIRCLE_LINK).click()
    sleep(5)