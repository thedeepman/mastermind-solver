Feature: Generating all possible permutations

  Scenario Outline: Permutations with repeats
    Given I setup a game with "<slots>" slots and "<colors>" colors
    When I generate all permutations with repeats
    Then total possibilities should be "<answer>"

    Examples:
      | slots | colors | answer |
      | 2     | 3      | 9      |
      | 3     | 3      | 27     |
      | 4     | 6      | 1296   |

  Scenario Outline: Permutations without repeats
    Given I setup a game with "<slots>" slots and "<colors>" colors
    When I generate all permutations without repeats
    Then total possibilities should be "<answer>"

    Examples:
      | slots | colors | answer |
      | 2     | 3      | 6      |
      | 3     | 3      | 6     |
      | 4     | 6      | 360   |