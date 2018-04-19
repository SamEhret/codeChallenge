import sys
import re
from treeClass import node
from inputFunctions import processInput

# Creates nodes after making list
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