class MyLinkedListQueue:
    def __init__(self, value = None):
        if value != None:
            newNode = self.newNode(value)
            self.first = newNode
            self.last = newNode
            self.length = 1
        else:
            self.first = None
            self.last = None
            self.length = 0

    def newNode(self, value):
        newNode = {
            "value": value,
            "next": None
        }
        return newNode

    def enqueue(self, value):
        newNode = self.newNode(value)
        if self.length == 0:
            self.first = newNode
        else:
            self.last["next"] = newNode

        self.last = newNode
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        self.first = self.first["next"]
        self.length -= 1

    def peek(self):
        if self.length == 0:
            return None
        return self.first["value"]

    def printLinkedList(self):

        myArray = []
        currentNode = self.first

        while currentNode != None:
            myArray.append(currentNode["value"])
            currentNode = currentNode["next"]

        return myArray

if __name__ == '__main__':

    myLinkedListQueue = MyLinkedListQueue(5)
    print(myLinkedListQueue.printLinkedList())
    print(myLinkedListQueue.peek())
    myLinkedListQueue.enqueue(10)
    print(myLinkedListQueue.printLinkedList())
    print(myLinkedListQueue.peek())
    myLinkedListQueue.enqueue(15)
    print(myLinkedListQueue.printLinkedList())
    print(myLinkedListQueue.peek())
    myLinkedListQueue.dequeue()
    print(myLinkedListQueue.printLinkedList())
    print(myLinkedListQueue.peek())
