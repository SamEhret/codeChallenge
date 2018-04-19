import sys
from treeFunctions import buildTree
from inputFunctions import getInput, isValid, processInput

inputString = getInput()
if isValid(inputString):
    finishedTree = buildTree(inputString)
    print(finishedTree)
else:
    print('Invalid input')
    sys.exit()