# Mastermind Solver
[Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game)) is a two-player board game. This is an attempt to programmatically solve it.

### Approach
- Generate all possible permutations of the solution
- Pick a random permutation
  - Check against previous to see if this permutation is valid
  - If not, delete this permutation and pick another
- Use the random permutation that does not violate previous results as the guess
- If there is no red (right color, right position) in the result, then all permutations that contain the given colors in their position for this guess can be eliminated

### ToDo
- Check if picking random permutations verses a more discriminatory approach yields better results 

### Instructions
Standard python setup
- Clone repo
- Create virtual environment or let IDE set it up
- Run "pip install -r requirements.txt"
- Run "behave" to run BDD tests
