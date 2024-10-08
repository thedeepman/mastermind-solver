Feature: Check if this permutation is valid against a previous result

  Scenario Outline: Simple validation without repeats
    Given I give it permutation "<option>" and previous result "<previous_option>" with "<red>" reds and "<white>" whites
    When I check if this permutation is valid
    Then the result will be "<answer>"

    Examples:
      | option  | previous_option | red | white | answer |
      | 0,1,2,3 | 1,2,3,4         | 0   | 3     | True   |
      | 3,2,1,0 | 4,2,5,0         | 3   | 0     | False  |
      | 3,2,1,0 | 4,2,5,0         | 2   | 0     | True   |

  Scenario Outline: Validation with repeats
    Given I give it permutation "<option>" and previous result "<previous_option>" with "<red>" reds and "<white>" whites
    When I check if this permutation is valid
    Then the result will be "<answer>"

    Examples:
      | option  | previous_option | red | white | answer |
      | 1,1,2,3 | 1,2,3,4         | 1   | 2     | True   |
      | 3,4,1,0 | 4,4,5,0         | 3   | 0     | False  |