from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

search_field = (By.ID, 'search')
search_icon = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
cart_icon = (By.XPATH,"//div[@data-test='@web/CartIcon']")
HEADER = (By.CSS_SELECTOR,"[class*='UtilityHeaderWrapper-']")
HEADER_LINK = (By.CSS_SELECTOR,"[data-test*='@web/GlobalHeader/UtilityHeader']")


@given('Open target page')
def open_target_main(context):
    context.driver.get("https://www.target.com/")
    sleep(5)


@when('Search for {items}')
def search_product(context,items):
    context.driver.find_element(*search_field).send_keys(items)
    context.driver.find_element(*search_icon).click()
    sleep(5)


@when('click target card Icons')
def step_impl(context):
    context.driver.find_element(*cart_icon).click()
    sleep(5)


@when('open singing form')
def step_impl(context):
    context.driver.find_element( By.XPATH, "//span[contains(@class,'styles__LinkText')]" ).click()
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(5)


@then("Verify header in shown")
def step_impl(context):
    header = context.driver.find_element(*HEADER)
    print(header)


@then("Verify header has {expected_amount} link")
def step_impl(context,expected_amount):
    expected_amount = int(expected_amount)
    header_link = context.driver.find_elements(*HEADER_LINK)
    assert len(header_link)  == expected_amount ,f"expected {expected_amount} but received  {len(header_link)} link"

