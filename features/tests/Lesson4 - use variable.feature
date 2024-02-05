Feature: Target.com search test (lesson 4)

  Scenario: user can reach for product on Target
    Given Open Target page
    When Search for items
    Then Search result for items are shown

#  Scenario: user can search for mug on Target
#    Given Open Target main page
#    When Search for mug
#    Then Search result for mug are shown
