import sys
import re
from treeClass import node
from inputFunctions import processInput

# Creates nodes after making list
# Each valid item in list is created as new node with
# current reference parent set as the parent
# "(" moves parent reference down, ")" moves parent reference up
def buildTree(inputString):
    processedString = processInput(inputString)
    root = node('')
    newRoot = root
    for item in processedString:
        if item == '(':
            newRoot = newRoot.children[-1]
        elif item == ')':
            newRoot = newRoot.parent
        else:
            newRoot.children.append(node(item))
            newRoot.children[-1].parent = newRoot
    return root