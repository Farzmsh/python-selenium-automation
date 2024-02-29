Feature: Tests for main page UI
  Scenario: Verify header in shown
    Given open target main page
    When Hover over signin
    Then Verify signin arrow shown
