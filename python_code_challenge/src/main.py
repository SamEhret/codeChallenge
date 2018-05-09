import sys
from treeFunctions import buildTree
from inputFunctions import getInput, isValid

# If string input is valid, create tree and print
inputString = getInput()
if isValid(inputString):
    finishedTree = buildTree(inputString)
    print(finishedTree)
else:
    print('Invalid input')
    sys.exit()