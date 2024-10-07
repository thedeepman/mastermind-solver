Feature: Check if this permutation is valid against a previous result

  Scenario Outline: Validate for simple 4x4
    Given I give it permutation "<option>" and previous result "<previous_option>" with "<red>" reds and "<white>" whites
    When I check if this permutation is valid
    Then the result will be "<answer>"

    Examples:
      | option  | previous_option | red | white | answer |
      | 0,1,2,3 | 1,2,3,0         | 0   | 3     | True   |
      | 3,2,1,0 | 1,2,3,0         | 3   | 0     | False  |