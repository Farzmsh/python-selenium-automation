from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Search result for {expected_result} are shown')
def verify_search_results_correct(context,expected_result):
    actual_test = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_result in actual_test, f"{expected_result} is not {actual_test}"
    print("Test case passed")


@then('Page URL has search term {expected_url}')
def verify_search_results_correct(context,expected_url):
    url = context.driver.current_url
    assert expected_url in url, f"{expected_url} is not{url}"
    print("Test case passed")


@then('verify there are 5 benefit boxes in Target circle')
def verify_search_results_correct(context):
    Benefit_box = context.driver.find_elements(By.XPATH, "//li[contains(@class,'styles__BenefitCard-sc-9mx6dj-2')]")
    assert len(Benefit_box) == 5, f"there are {len(Benefit_box)} benefit boxes in Target circle "
    print("Test case passed")


