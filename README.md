# seed-bdd-python
Seed Project for using Behavior Driven Development in Python

Uses [behave](https://behave.readthedocs.io/en/stable/) for BDD using [Gherkin](https://cucumber.io/docs/gherkin/reference/) syntax

Project Structure
- Gherkin features named .feature in 'features' folder
- 'steps' folder inside 'features' containing step definitions
  - Step definitions are .py files
- A feature can have multiple step definition files and vice versa
  - Can reuse steps across features and other optimization

### Instructions
Standard python setup
- Clone repo
- Create virtual environment or let IDE set it up
- Run "pip install -r requirements.txt"
- Run "behave" to see example scenarios run and results in console
- Create new feature or add to existing feature, run "behave", see the tests fail
  - Update step definitions and then update production code to get tests to pass

### Future
- Create branches for specific types of projects like UI, Data, API,...