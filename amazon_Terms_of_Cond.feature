# Created by carte at 6/3/2022
Feature: Tests applications from Terms of Conditions


  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window
    And User can switch back to original


