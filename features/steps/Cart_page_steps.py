from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

view_card_btn = (By.CSS_SELECTOR, "a[href='/cart'][class*='styles__StyledBaseButtonInternal']")
cart_item_title = (By.CSS_SELECTOR,"div[data-test='cartItem-title']")


@then('verify the item\'s cart')
def verify_item(context):
    quantity = context.driver.find_element( By.XPATH, "//h2[@data-test='cart-summary-title']" ).text
    assert quantity in "Order summary", f"The quantity{quantity} is not{quantity}"
    sleep( 5 )
    print( "****    Cart has individual cart items  ****" )


@then('Verify \'your cart empty\' message is shown')
def verify_cart_empty_message(context):
    actual_text = context.app.cart_page.verify_cart_empty_message()
    print(actual_text)


@then('Verify cart has {item_for_search}')
def step_impl(context,item_for_search):
    actual_item_in_the_cart = context.driver.find_element(*cart_item_title).text
    print(actual_item_in_the_cart)
    assert context.products_name_side_nav in actual_item_in_the_cart, f"{item_for_search} is not in cart"
    print("test passed")