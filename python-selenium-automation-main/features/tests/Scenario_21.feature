Feature: Test Scenarios for Product functionality

  Scenario: User can see titles and pictures on each product inside the off plan page
    Given Open the main page
    When Enter email
    When Enter password
    When Click on Continue
    When Click on off plan
    Then Verify the Off Plan page is opened
    Then Verify each product on this page contains a title and picture visible