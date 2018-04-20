# codeChallenge
>Coding challenge with unittests included.
Given a string input that uses parenthesis to seperate levels, create a tree where each level is indented with a "-". Results should be printed alphabeticalls by level. Also includes unittests for each code file.

#### Example input:
```'(test(dog,carry(talent))table)'```

#### Example Output:
```
table
test
- carry
-- talent
- dog
```

#### Assumptions:
1. String sorting is used to determine order
2. "(", ")" and "," are only separators and are never actual data
3. Valid input starts with "(" and ends with ")"

# Getting Started
#### Prerequisities
For running unittests, the project requires the installation of pytest. To install:
##### Installing pytest
`pip install pytest`
##### Running pytest
`py.test testName.py`
