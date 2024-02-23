Feature: Target.com website

  Scenario: user can search for coffee on target
    Given Open target main page
    When Search for coffee
    Then Search result for coffee are shown
    Then Page URL has search term coffee


  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When click on card Icons
    Then Verify 'your cart empty' message is shown


  Scenario Outline: user can search for a product on target
    Given Open target main page
    When Search for <items>
    Then Search result for <expected_result> are shown
    Then Page URL has search term <expected_url>
    Examples:
    |items      |expected_result    |expected_url     |
    |mug        |mug                |mug               |
    |Coffee mug |Coffee mug         |Coffee+mug       |
    |tea        |tea                |tea              |


  Scenario: Verify header in shown
    Given Open target main page
    Then Verify header in shown


  Scenario: Verify header has 5 link
    Given Open target main page
    Then Verify header has 5 link


  Scenario: verify there are 5 benefit boxes in Target circle
    Given Open target main page
    When  open target circle page
    Then  verify there are 5 benefit boxes in Target circle


  Scenario Outline: Create a test case to verify Target Help UI
    Given Open help page
    Then  Verify there are 6 boxes in Help page
    Then  Verify there are "contact us" and "product recalls are in Help page
    Then  Verify '<expected_result>' is present of <element>
    Examples:
    |element                                                 |expected_result          |
    |//h2[@class='custom-h2']                                |Target Help              |
    |//div[text()='track an order']                          |track an order           |
    |//div[text()='view current promotions']                 |view current promotions  |
    |//div[text()='pickup & delivery']                       |pickup & delivery        |
    |//div[text()='returns & receipts']                      |returns & receipts       |
    |//div[text()='check GiftCard balance']                  |check GiftCard balance   |
    |//div[text()='fix an issue']                            |fix an issue             |
    |//h3[@class='custom-h3' and text()='contact us']        |contact us               |
    |//h3[@class='custom-h3' and text()='product recalls']   |product recalls          |
    |//h2[text()='Browse all Help pages']                    |Browse all Help pages    |



  Scenario Outline:  Verify that every product on Target search results page has
    Given  Open target main page
    When   looking for <item_for_search>
    And    click to add to the cart
    And    store product name
    And    confirm add to card right side the page
    And    open target cart page
    Then   Verify cart has <item_for_search>


    Examples:
      |item_for_search                                |
      |Women's Cropped Zip-Up Hoodie                  |
      |denizen levis mens                             |


  Scenario Outline:  Create a test case with a loop
    Given  Open target main page
    When   looking for <item_for_search>
    And    click to add to the cart
    And    store product name
    And    open product details
    Then   verify user can click through color

    Examples:
      |item_for_search                                |
      |Women's Cropped Zip-Up Hoodie                 |
      |denizen levis mens                             |


    Scenario:  Verify every item has name and img
    Given  Open target main page
    When   looking for AirPods
    Then    Verify every item has name and img
