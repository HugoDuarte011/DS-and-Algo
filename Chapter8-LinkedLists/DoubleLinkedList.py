class MyLinkedList:
    def __init__(self, head):
        self.head = {
            "value": head,
            "next": None,
            "prev": None
            }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newNode = {
            "value": value,
            "next": None,
            "prev": None
        }
        newNode["prev"] = self.tail
        self.tail["next"] = newNode
        self.tail = newNode
        self.length += 1
        return self

    def prepend(self, value):
        newNode = {
            "value": value,
            "next": None,
            "prev": None
        }
        self.head["prev"] = newNode
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
            "next": None,
            "prev": None
        }

        currentNode = self.head
        currentIndex = 1

        while currentNode != None:
            if currentIndex == index:
                newNode["next"] = currentNode["next"]
                newNode["prev"] = currentNode
                currentNode["next"]["prev"] = newNode
                currentNode["next"] = newNode
                self.length += 1
            currentIndex += 1
            currentNode = currentNode["next"]
        return self

    def myDelete(self, index):
        ##Check Params

        newNode = {
            "value": None,
            "next": None,
            "prev": None
        }

        leader = self.traverseToIndex(index-1)
        follower = leader["next"]
        secondFollower = follower["next"]

        leader["next"] = secondFollower
        secondFollower["prev"] = leader
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
        follower = leader["next"]
        leader["next"] = newNode
        newNode["prev"] = leader
        newNode["next"] = follower
        follower["prev"] = newNode
        self.length += 1
        return self

    def traverseToIndex(self, index):
        counter = 0
        currentNode = self.head

        while counter != index:
            currentNode = currentNode["next"]
            counter += 1

        return currentNode

    def reverse(self):
        auxHead = self.head

        currentNode = self.tail

        # while currentNode != None:



if __name__ == '__main__':

    myLinkedList = MyLinkedList(10)
    print(myLinkedList.printLinkedList())
    myLinkedList.append(12)
    print(myLinkedList.printLinkedList())
    myLinkedList.append(16)
    print(myLinkedList.printLinkedList())
    myLinkedList.prepend(1)
    print(myLinkedList.printLinkedList())
    myLinkedList.myInsert(1, 9)
    print(myLinkedList.printLinkedList())
    myLinkedList.lessonInsert(1, 7)
    print(myLinkedList.printLinkedList())
    myLinkedList.myDelete(2)
    print(myLinkedList.printLinkedList())


