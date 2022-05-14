# Created by carte at 5/14/2022
Feature: Tests elements on Best Sellers Page


  Scenario: User sees correct amount of links
    Given Open BestSellers page
    Then Verify there are 5 header links

