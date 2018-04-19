class node(object):
    def __init__(self, value, parent=None, children=[]):
        self.value = value
        self.parent = None
        self.children = []

    def getData(node):
        return node.value

    def __str__(self, level=-1):
        printString = '-' * level + str(self.value) + '\n'
        sortedChildren = sorted(self.children, key=node.getData)
        for child in sortedChildren:
            printString += child.__str__(level + 1)
        return printString