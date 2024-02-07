from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('verify the item\'s cart')
def verify_item(context):
    quantity = context.driver.find_element( By.XPATH, "//h2[@data-test='cart-summary-title']" ).text
    assert quantity in "Order summary", f"The quantity{quantity} is not{quantity}"
    sleep( 5 )
    print( "****    Cart has individual cart items  ****" )


@then('Your cart is empty')
def step_impl(context):
    cart_is_empty = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    assert "Your cart is empty" in cart_is_empty, f"Error "
    print()
    print("*****    'Your cart is empty' message is shown      *****" )