class node(object):
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

    # Returns each node value for sorting
    def getData(node):
        return node.value

    # Recursively creates final string
    # For each level down in the tree, level counter is increased
    # Children of the same level are sorted with string sort from getData
    def __str__(self, level=-1):
        printString = '-' * level + str(self.value) + '\n'
        sortedChildren = sorted(self.children, key=node.getData)
        for child in sortedChildren:
            printString += child.__str__(level + 1)
        return printString