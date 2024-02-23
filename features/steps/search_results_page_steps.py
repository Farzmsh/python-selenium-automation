from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then('Search result for {expected_result} are shown')
def verify_search_results_correct(context,expected_result):
    context.app.search_results_page.verify_search_results_correct(expected_result)


@then('Page URL has search term {expected_part_url}')
def verify_search_results_page_url(context,expected_part_url):
    context.app.search_results_page.verify_search_results_page_url(expected_part_url)


@then('verify there are 5 benefit boxes in Target circle')
def verify_search_results_correct(context):
    Benefit_box = context.driver.find_elements(By.XPATH, "//li[contains(@class,'styles__BenefitCard-sc-9mx6dj-2')]")
    assert len(Benefit_box) == 5, f"there are {len(Benefit_box)} benefit boxes in Target circle "
    print("Test case passed")

