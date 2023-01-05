##Implement a Hash Table

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


if __name__ == '__main__':
    myHashTable = MyHashTable(50)
    myHashTable.set('grapes', 10000)
    myHashTable.set('apples', 54)
    myHashTable.set('oranges', 2)
    print(myHashTable.keys())

    ##print(myHashTable.data)
