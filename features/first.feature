Feature: Example

  Scenario: Test that this works
    Given I have a method
    When I call it
    Then the result should be 0

  Scenario Outline: Testing with multiple data inputs
    Given I have a new method
    When I give it "<num1>" and "<taskname>"
    Then the result should be "<answer>"

    Examples:
      | num1 | taskname | answer |
      | 2    | add      | 4      |
      | 4    | multiply | 16     |