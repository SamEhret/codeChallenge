import sys
import re
from treeClass import node
from inputFunctions import processInput

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
            newRoot.children[-1].parent = newRoot
    return root