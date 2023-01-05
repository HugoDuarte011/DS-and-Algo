class MyHashTable:
    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash

    def set(self, key, value):
        address = self._hash(key)
        if self.data[address] == None:
            self.data[address] = []
        self.data[address].append([key, value])

    def get(self, key):
        address = self._hash(key)
        currentBucket = self.data[address]
        if currentBucket != None:
            for i in range(len(currentBucket)):
                if currentBucket[i][0] == key:
                    return currentBucket[i][1]
        return None

    def keys(self):
        keysArray = []
        for i in range(len(self.data)):
            if self.data[i] != None:
                keysArray.append(self.data[i][0][0])
        return keysArray



    def myFirstRecurringCharacter(self, array):

        aux = []

        for i in array:
            if aux.__contains__(i):
                return i
            aux.append(i)

        return "There's no recurring character!"

    def lessonFirstRecurringCharacter(self, array):

        for i in array:
            if self.get(chr(i)):
                return i
            self.set(chr(i), True)

        return "There's no recurring character!"
if __name__ == '__main__':
    myArray = [2, 5, 1, 2, 3, 5, 1, 2, 4]
    ##myArray = [2, 1, 1, 2, 3, 5, 1, 2, 4]
    ##myArray = [2, 3, 4, 5]

    myHashTable = MyHashTable(len(myArray))

    print(myHashTable.lessonFirstRecurringCharacter(myArray))

