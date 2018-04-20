# codeChallenge
>Coding challenge with unit tests included.

Given a string input that uses parenthesis to seperate levels, create a tree where each level is indented with a "-". Results should be printed alphabetically by level. Also includes unit tests for each code file.

#### Example input:
```(test(dog,carry(talent))table)```

#### Example Output:
```
table
test
-carry
--talent
-dog
```

#### Assumptions:
1. String sorting is used to determine order
2. "(", ")" and "," are only separators and are never actual data
3. Valid input starts with "(" and ends with ")"

# Getting Started
## Prerequisities
python 3 is required and can be installed [here](https://www.python.org/downloads/)

Pytest is required for running unit tests. Documentation for pytest can be found [here](https://docs.pytest.org/en/latest/contents.html)
#### Installing pytest
`pip install pytest`
#### Running pytest
`py.test testName.py`
#### Valid test files
mainTests.py

inputFunctionsTests.py

treeFunctionsTests.py

treeClassTests.py

## Running the program
The program will be run from the main.py file. Upon start up, user will be asked to input a valid string, and if no value is passed in, the program will run the default string.
#### Running codeChallenge
```python3 main.py```
