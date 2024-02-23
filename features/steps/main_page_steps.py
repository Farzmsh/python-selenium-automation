from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


HEADER = (By.CSS_SELECTOR,"[class*='UtilityHeaderWrapper-']")
HEADER_LINK = (By.CSS_SELECTOR,"[data-test*='@web/GlobalHeader/UtilityHeader']")
my_product = (By.XPATH,"//a[@href='/p/women-s-cropped-zip-up-hoodie-wild-fable/-"
                       "/A-81540287?preselect=81403401#lnk=sametab']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
add_to_cart_side_btn = (By.CSS_SELECTOR, "[data-test='shippingButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='styles__StyledHeading']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='shippingButton']")


@given('Open target main page')
def open_target_main(context):
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context,product):
    context.app.header.search_product()
    sleep(6)


@when('click on card Icons')
def step_impl(context):
    context.app.header.click_cart_icon()
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
    assert len(header_link) == expected_amount,f"expected {expected_amount} but received  {len(header_link)} link"


# @when("looking for {item_for_search}")
# def step_impl(context,item_for_search):
#     # find the search box
#     context.driver.find_element(*search_field).send_keys(item_for_search)
#     # find the item and click on search
#     context.driver.find_element(*search_icon).click()
#     sleep(10)


@when('click to add to the cart')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(10)


@when('store product name')
def store_product_name(context):
    context.wait.until(EC.presence_of_element_located(SIDE_NAV_PRODUCT_NAME), message='The side navigation is not open')
    context.products_name_side_nav = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(context.products_name_side_nav)


@when('confirm add to card right side the page')
def confirm_add_to_cart(context):
    context.driver.find_element(*add_to_cart_side_btn).click()
    sleep(2)


@given("click on signin text on main page")
def click_signin_icon(context):
    context.app.header.click_sign_in_text()


@given ("verify navigation side to click on signin")
def right_side_navigation_menu(context):
    context.app.sign_in_page.right_side_navigation_menu()


