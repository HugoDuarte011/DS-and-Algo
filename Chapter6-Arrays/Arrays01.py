
class MyArray:
    def __init__(self):
        self.lenght = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.lenght] = item
        self.lenght+=1
        return self.data

    def pop(self):
        val = self.data[self.lenght-1]
        del self.data[self.lenght-1]
        self.lenght -= 1
        return val

    def deleteAtIndex(self, index):
        val = self.shiftItem(index)
        return val

    def shiftItem(self, index):
        val = self.data[index]
        for i in range(index, self.lenght - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.lenght-1]
        self.lenght -= 1
        return val

if __name__ == '__main__':

    myArray = MyArray()
    print(myArray.push(10))
    print(myArray.push(15))
    print(myArray.push(20))
    print(myArray.push(25))
    print(myArray.push(30))
    print(myArray.push(35))
    print(myArray.get(3))
    print(myArray.pop())
    print(myArray.deleteAtIndex(3))
    print(myArray.data)
