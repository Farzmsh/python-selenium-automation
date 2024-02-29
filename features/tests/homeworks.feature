Feature: Execute homeworks
  Scenario:
    Given Open target main page
    And  click on signin text on main page
    And  verify navigation side to click on signin
    When  Input email and password

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open target main page
    And  click on signin text on main page
    And  verify navigation side to click on signin
    When Store original windows
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window
    And switch back to original window

  Scenario: User can select Help topic
    Given Open Help page for Returns
    Then Verify Returns page opened
    When Select Help topic Gift Cards
    Then Verify Target GiftCard balance page opened

  Scenario: Verifies that user can't login with invalid username and password
    Given Open target main page
    And  click on signin text on main page
    And  verify navigation side to click on signin
    When  Input email and password and click on signin button
    Then   Verify 'Please enter a valid password' message is shown
