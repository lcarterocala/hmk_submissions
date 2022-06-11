# Created by carte at 5/7/2022
Feature: Test the empty cart case


  Scenario: Your Shopping Cart is empty' shown if no product added
    Given Open Amazon page
    When Cart is clicked
    Then Verify Your Shopping Cart is empty

  Scenario: User verify that product can be added to the cart
    Given Open Amazon page
    When Search for rings
    And Click on the first product
    And Click on Add to Cart button
    Then Verify 1 item(s) in cart


   # When Search for Tritan Farm to table Pitcher
   # And Click on the first product
   # And Click on Add to cart button
   # And Open cart page