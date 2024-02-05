from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#-----------------------------------------------------------------------------
@given('Open Target page')
def step_impl(context):
    context.driver.get("https://www.target.com/")
    sleep(2)

@when('Search for {product}')
def step_impl(context, product):
    print(product)
    context.driver.find_element(By.ID, "#searchMobile" ).send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton'] ").click()
    sleep(6)


@then('Search result for items are shown')
def step_impl(context):
    actual_result = context.driver.find_element(By.XPATH, "")


