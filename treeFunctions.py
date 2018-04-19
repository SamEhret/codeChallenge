import sys
import re
from treeClass import node

# Take input or give default input
def getInput():
    inputString = input('Please enter the string to process')
    if not inputString:
        inputString = '(id,created,employee(id,firstname,employeeType(id),lastname),location)'
    return inputString

# Check that nesting in () is valid
def isValid(inputString):
    leftParen = 0
    rightParen = 0
    if inputString.count('(') != inputString.count(')'):
        return False
    elif inputString[0] != '(' or inputString[-1] != ')':
        return False
    return True

# Process inputString to list
def processInput(inputString):
    inputString = re.search(r'\((.+)\)', inputString)
    inputString = inputString[1]
    inputString = re.split('([(),])', inputString)
    while ',' in inputString or '' in inputString:
        for val in inputString:
            if val == ',' or val == '':
                del inputString[inputString.index(val)]
    return inputString

# Creates nodes
def buildTree(inputString):
    processedString = processInput(inputString)
    root = node('')
    newRoot = root
    for val in processedString:
        if newRoot is None:
            newRoot = root
        elif val == '(':
            newRoot = newRoot.children[-1]
        elif val == ')':
            newRoot = newRoot.parent
        else:
            newRoot.children.append(node(val))
            newRoot.children[0].parent = newRoot
    return root