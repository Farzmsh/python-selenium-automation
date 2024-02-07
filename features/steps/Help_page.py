from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIX_BOXES = (By.XPATH,"//div[@class='box-column']//div[contains(@class,'boxSmall')]")


@given("Open help page")
def step_impl(context):
    context.driver.get("https://help.target.com/help")
    sleep(0)


@then('Verify there are 6 boxes in Help page')
def step_impl(context):
    would_you_like_boxes = context.driver.find_elements(*SIX_BOXES)
    assert len(would_you_like_boxes) == 6,f'There are not 6 boxes in Help page'
    print("Test passed")


@then('Verify there are "contact us" and "product recalls are in Help page')
def step_impl(context):
    result = context.driver.find_elements(By.XPATH,"//div[contains(@class,'grid_4 boxSmallr')]//h3[@class='custom-h3']")
    assert len(result) == 2,f'one of item is missing'
    print("Test passed")


@then("Verify '{expected_result}' is present of {element}")
def step_impl(context, expected_result, element):
    actual_result = context.driver.find_element(By.XPATH, element).text
    assert actual_result == expected_result,f"Expected result '{expected_result}' not found for element '{element}' "
    print("Test passed")



