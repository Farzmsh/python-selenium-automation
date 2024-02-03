from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#-----------------------------------------------------------------------------

user_name = "User_name"
password = "<PASSWORD>"
item_TCIN = "TCIN: 88691673"

#-----------------------------------------------------------------------------

@given('Open Target web page')
def step_impl(context):
    context.driver.get("https://www.target.com/" )
    sleep( 2 )


@when('click target card Icon')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@data-test='@web/CartIcon']").click()
    sleep(5)

@then('Your cart is empty')
def step_impl(context):
    cart_is_empty = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    assert "Your cart is empty" in cart_is_empty, f"Error "
    print()
    print("*****    'Your cart is empty' message is shown      *****" )

#-----------------------------------------------------------------------------
# @given('Open Target web page')
# def step_impl(context):
#     context.driver.get("https://www.target.com")
#     sleep(5)

@when('Search for item and add the item into the cart')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']" ).send_keys( item_TCIN )
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']" ).click()
    sleep(5)
    context.driver.find_element(By.XPATH, "//button[@data-test='chooseOptionsButton' and text()='Add to cart' ]" ).click()
    sleep(5)
    context.driver.find_element(By.XPATH,"//button[@data-test='shippingButton' and text()='Add to cart']").click()
    sleep(5)
    context.driver.find_element(By.XPATH, "//a[@href='/cart' and text()='View cart & check out']").click()
    sleep(5)


@then('verify the item\'s cart')
def verify_item(context):
    quantity = context.driver.find_element(By.XPATH, "//h2[@data-test='cart-summary-title']" ).text
    assert quantity in "Order summary",f"The quantity{quantity} is not{quantity}"
    sleep(5)
    print("****    Cart has individual cart items  ****")



# -------------------------------------------------------------
# @given('Verify Sign In form opened')
# def step_impl(context):
#     context.driver.get( "https://www.target.com/" )

@when('open singing form')
def step_impl(context):
    context.driver.find_element( By.XPATH, "//span[contains(@class,'styles__LinkText')]" ).click()
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(5)


@then('Target singnin page is open')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#username").send_keys(user_name)
    context.driver.find_element(By.CSS_SELECTOR, "#password" ).send_keys(password)
    sleep(2)
    context.driver.find_element(By.XPATH,"//button[@type='button' and text()='show']").click()
    sleep(2)
    context.driver.find_element( By.CSS_SELECTOR, "#login" ).click()
    print()
    print("*****    logged out user can access Sign In ********")
    sleep(6)