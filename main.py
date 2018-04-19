import sys
from treeFunctions import getInput, isValid, processInput, buildTree

inputString = getInput()
if isValid(inputString):
    finishedTree = buildTree(inputString)
    print(finishedTree)
else:
    print('Invalid input')
    sys.exit()