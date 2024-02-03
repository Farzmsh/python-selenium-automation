# Created by farzm at 1/29/2024
Feature: Target.com search test

  Scenario: user can search for product on target
    Given Open target main page
    When Search for Coffee
    Then Search result for Coffee are shown


