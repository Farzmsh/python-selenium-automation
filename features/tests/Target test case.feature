Feature: Target.com website

  Scenario: user can search for coffee on target
    Given Open target page
    When Search for Coffee
    Then Search result for Coffee are shown
    Then Page URL has search term Coffee


  Scenario: user can search for mug on target
    Given Open target page
    When Search for mug
    Then Search result for mug are shown
    Then Page URL has search term mug


  Scenario Outline: user can search for a product on target
    Given Open target page
    When Search for <items>
    Then Search result for <expected_result> are shown
    Then Page URL has search term <expected_url>
    Examples:
    |items      |expected_result    |expected_url     |
    |mug        |mug                |mug               |
    |Coffee mug |Coffee mug         |Coffee+mug       |
    |tea        |tea                |tea              |


  Scenario: Verify header in shown
    Given Open target page
    Then Verify header in shown


  Scenario: Verify header has 5 link
    Given Open target page
    Then Verify header has 5 link


  Scenario: verify there are 5 benefit boxes in Target circle
    Given Open target page
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







