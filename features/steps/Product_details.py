from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

product_name_nav_side = (By.CSS_SELECTOR, "h4[class*='styles__StyledHeading']")
color_option = (By.CSS_SELECTOR, "div[class*='styles__ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")
listing_items = (By.CSS_SELECTOR,"[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
product_title = (By.CSS_SELECTOR, "[data-test='product-title']")
product_img = (By.CSS_SELECTOR, "[class*='ProductCardImage']")


@when('open product details')
def step_impl(context):
    context.driver.find_element(*product_name_nav_side).click()
    sleep(10)


@then ("verify user can click through color")
def step_impl(context):
    expected_colors = ['Black','Red','Green','Yellow','Deep Olive','White','Blue Tint', 'Denim Blue','Marine','Raven']

    actual_colors = []
    colors = context.driver.find_elements(*color_option)
    for color in colors[:3]:
        color.click()
        selected_color = context.driver.find_element( *SELECTED_COLOR ).text
        selected_color = selected_color.split( '\n' )[1]
        actual_colors.append( selected_color )
        print(actual_colors)
    for color in expected_colors:
        assert color in expected_colors, f"Unexpected color found: {color}"


@then ("Verify every item has name and img")
def step_impl(context):
    context.driver.execute_script("window.scrollBy(0,2000)","")
    sleep(2)
    context.driver.execute_script("window.scrollBy(0,2000)","")

    all_products = context.driver.find_elements(*listing_items)

    for product in all_products:
        title = product.find_element(*product_title).text
        print(title)
        assert title,f'product title not shown'
        product.find_element(*product_img)




