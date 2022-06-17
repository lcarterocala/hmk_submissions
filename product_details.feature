# Created by carte at 5/31/2022
Feature: Tests for product page


  Scenario: User can select colors
    Given Open Amazon product B07QYSZBGX page
    Then Verify user can click through colors


  Scenario: User opens product page and sees the deals
    Given Open Amazon product B074TBCSC8 page
    When Hover over New Arrivals
    Then Verify that user sees deals
