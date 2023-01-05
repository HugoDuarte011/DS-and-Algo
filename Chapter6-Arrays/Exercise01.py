
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

    '''
    ##With implemented array
    myArray = MyArray()
    
    string = "Hi, My Name Is Hugo"
    lenString = len(string)
    
    for i in range(1, lenString+1):
        print(string[lenString - i])
        myArray.push(string[lenString - i])

    print(str(myArray))'''

    inOrderString = "Hi, My Name Is Hugo!"
    reversedString = ""
    lenString = len(inOrderString)

    for i in range(1, lenString+1):
        reversedString = reversedString+inOrderString[lenString - i]

    print(reversedString)