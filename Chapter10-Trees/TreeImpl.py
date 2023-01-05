from binarytree import tree as trr

class Node:
    def __init__(self, value = None):
        if value == None:
            return None
        self = {

        }

class Tree:
    def __init__(self, value = None):
        if value == None:
            return None
        newNode = self.newNode(value)
        self.root = newNode

    def newNode(self, value):
        if type(value) != type(0):
            return None
        newNode = {
            "value": value,
            "left": None,
            "right": None,
            "parent": None
        }
        return newNode

    def insert(self, value):
        newNode = self.newNode(value)
        if self.root == None:
            self.root = newNode
            return newNode
        currNode = self.root
        while currNode != None:
            if newNode["value"] == currNode["value"]:
                print("Can't have more than 1 node with the same value!")
                return None
            elif newNode["value"] < currNode["value"]:
                if currNode["left"] == None:
                    currNode["left"] = newNode
                    newNode["parent"] = currNode
                    break
                else:
                    currNode = currNode["left"]
            elif newNode["value"] > currNode["value"]:
                if currNode["right"] == None:
                    currNode["right"] = newNode
                    newNode["parent"] = currNode
                    break
                else:
                    currNode = currNode["right"]

    def lookup(self, value):
        if self.root == None:
            return None
        currNode = self.root
        while currNode != None:
            if value == currNode["value"]:
                return currNode
            elif value < currNode["value"]:
                    currNode = currNode["left"]
            elif value > currNode["value"]:
                    currNode = currNode["right"]

    def remove(self, value):
        if self.root == None:
            return None
        currNode = self.root
        parentNode = currNode
        while currNode != None:
            if value == currNode["value"]:
                if currNode["right"] == None:
                    if parentNode == None:
                        self.root = currNode["left"]
                    else:
                        if currNode["value"] < parentNode["value"]:
                            parentNode["left"] = currNode["left"]
                        elif currNode["value"] > parentNode["value"]:
                            parentNode["right"] = currNode["right"]
                elif currNode["right"]["left"] == None:
                    currNode["right"]["left"] == currNode["left"]
                    if parentNode == None:
                        self.root = currNode["right"]
                    else:
                        if currNode["value"] < parentNode["value"]:
                            parentNode["left"] = currNode["right"]
                        elif currNode["value"] > parentNode["value"]:
                            parentNode["right"] = currNode["right"]
                else:
                    leftMost = currNode["right"]["left"]
                    leftMostParent = currNode["right"]
                    while leftMost["left"] == None:
                        leftMostParent = leftMost
                        leftMost = leftMost["left"]
                    leftMostParent["left"] = leftMost["right"]
                    leftMost["left"] = currNode["left"]
                    leftMost["right"] = currNode["right"]
                    if parentNode == None:
                        self.root = leftMost
                    else:
                        if currNode["value"] < parentNode["value"]:
                            parentNode["left"] = leftMost
                        elif currNode["value"] > parentNode["value"]:
                            parentNode["right"] = leftMost


            elif value < currNode["value"]:
                    parentNode = currNode
                    currNode = currNode["left"]
            elif value > currNode["value"]:
                    parentNode = currNode
                    currNode = currNode["right"]
if __name__ == '__main__':

    myTree = Tree(53)
    print(myTree)
    myTree.insert(31)
    myTree.insert(52)
    myTree.insert(10)
    myTree.insert(14)
    myTree.insert(73)
    myTree.insert(61)
    myTree.insert(93)
    # myTree.insert(73)
    myTree.insert(87)
    myTree.insert(79)
    print(myTree.lookup(99))
