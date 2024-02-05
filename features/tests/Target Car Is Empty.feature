# Created by farzm at 1/30/2024
Feature: Target.com cart is empty
  # Enter feature description here

  Scenario: Verify the Target cart is empty
  Given Open Target web page
  When click target card Icon
  Then Your cart is empty

#------------------------------------------------------

  Scenario: Add an item Target’s product
  Given Open Target web page
  When Search for Coffee
  Then verify the item's cart

#------------------------------------------------------

  Scenario: Verify Sign In form opened
  Given Open Target web page
  When open singing form
  Then Target singnin page is open



