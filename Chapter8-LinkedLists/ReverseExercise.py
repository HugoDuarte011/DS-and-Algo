class MyLinkedList:
    def __init__(self, head):
        self.head = {
            "value": head,
            "next": None
            }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newNode = {
            "value": value,
            "next": None
        }
        self.tail["next"] = newNode
        self.tail = newNode
        self.length += 1
        return self

    def prepend(self, value):
        newNode = {
            "value": value,
            "next": None
        }
        newNode["next"] = self.head
        self.head = newNode
        self.length += 1
        return self

    def printLinkedList(self):

        myArray = []
        currentNode = self.head

        while currentNode != None:
            myArray.append(currentNode["value"])
            currentNode = currentNode["next"]

        return myArray

    def myInsert(self, index, value):
        if index <= 0:
            return self.prepend(value)
        elif index >= self.length:
            return self.append(value)

        newNode = {
            "value": value,
            "next": None
        }

        currentNode = self.head
        currentIndex = 1

        while currentNode != None:
            if currentIndex == index:
                newNode["next"] = currentNode["next"]
                currentNode["next"] = newNode
                self.length += 1
            currentIndex += 1
            currentNode = currentNode["next"]
        return self

    def myDelete(self, index):
        ##Check Params

        newNode = {
            "value": None,
            "next": None
        }
        leader = self.traverseToIndex(index-1)
        holdingPointer = leader["next"]
        leader["next"] = holdingPointer["next"]
        self.length -= 1
        return self

    def lessonInsert(self, index, value):
        ##Check Params
        if index <= 0:
            return self.prepend(value)
        elif index >= self.length:
            return self.append(value)

        newNode = {
            "value": value,
            "next": None
        }
        leader = self.traverseToIndex(index-1)
        holdingPointer = leader["next"]
        leader["next"] = newNode
        newNode["next"] = holdingPointer
        self.length += 1
        return self

    def traverseToIndex(self, index):
        counter = 0
        currentNode = self.head

        while counter != index:
            currentNode = currentNode["next"]
            counter += 1

        return currentNode

    def myReverse(self):

        if self.length <= 1:
            return self

        a = self.head
        self.tail = self.head
        b = a["next"]

        while b != None:
            c = b["next"]
            b["next"] = a
            a = b
            b = c
        self.head["next"] = None
        self.head = a

        return self

    def lessonReverse(self):

        if self.length <= 1:
            return self
        first = self.head
        self.tail = self.head
        second = first["next"]

        while second != None:
            temp = second["next"]
            second["next"] = first
            first = second
            second = temp
        self.head["next"] = None
        self.head = first

        return self

if __name__ == '__main__':

    myLinkedList = MyLinkedList(10)
    print(myLinkedList.printLinkedList())
    myLinkedList.append(5)
    print(myLinkedList.printLinkedList())
    myLinkedList.append(16)
    print(myLinkedList.printLinkedList())
    myLinkedList.prepend(1)
    print(myLinkedList.printLinkedList())
    myLinkedList.myInsert(3, 9)
    print(myLinkedList.printLinkedList())
    myLinkedList.lessonInsert(2, 7)
    print(myLinkedList.printLinkedList())
    myLinkedList.myDelete(2)
    print(myLinkedList.printLinkedList())
    myLinkedList.myReverse()
    print(myLinkedList.printLinkedList())


