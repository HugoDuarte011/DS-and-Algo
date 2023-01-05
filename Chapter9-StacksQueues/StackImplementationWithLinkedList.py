class MyLinkedListStack:
    def __init__(self, top):
        self.top = {
            "value": top,
            "next": None,
            "prev": None
            }
        self.bottom = self.top
        self.length = 1

    def newNode(self, value):
        newNode = {
            "value": value,
            "next": None,
            "prev": None
        }
        return newNode

    def append(self, value):
        newNode = self.newNode(value)
        newNode["prev"] = self.top
        self.top["next"] = newNode
        self.top = newNode
        self.length += 1
        return self

    def pop(self):
        aux = self.top["prev"]
        aux["next"] = None
        self.top = aux

    def peek(self):
        return self.top



    def printLinkedList(self):

        myArray = []
        currentNode = self.bottom

        while currentNode != None:
            myArray.append(currentNode["value"])
            currentNode = currentNode["next"]

        return myArray

if __name__ == '__main__':

    myLinkedListStack = MyLinkedListStack(10)
    print(myLinkedListStack.printLinkedList())
    myLinkedListStack.append(5)
    print(myLinkedListStack.printLinkedList())
    myLinkedListStack.append(16)
    print(myLinkedListStack.printLinkedList())
    myLinkedListStack.pop()
    print(myLinkedListStack.printLinkedList())
    print(myLinkedListStack.peek())


