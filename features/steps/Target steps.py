from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_main(context):
    context.driver.get("https://www.target.com/")
    sleep(5)


@when('Search for Coffee')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys("coffee")
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(10)


@then('Search result for Coffee are shown')
def verify_search_results_correct(context):
    actual_test = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert "coffee" in actual_test, f"Coffee is not {actual_test}"
    print("Test case passed")
