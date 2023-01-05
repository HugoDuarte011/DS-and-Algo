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

    def isEmpty(self):
        if len(self) == 0:
            return True
        else:
            return False

    def mergeSortedArrays(self, array1, array2):
        i = 0
        j = 0
        while self.lenght != (len(array1) + len(array2)):
            if i == len(array1) and j != len(array2):
                self.push(array2[j])
                j += 1
            elif j == len(array2) and i != len(array1):
                self.push(array1[i])
                i += 1
            elif array1[i] < array2[j]:
                self.push(array1[i])
                i += 1
            else:## array2[j] < array1[i]:
                self.push(array2[j])
                j += 1

        return self


if __name__ == '__main__':

    ##arr1 = [0, 3, 4, 31]
    arr1 = []
    arr2 = [4, 6, 30]

    merged = MyArray()
    
    mergedArrays = merged.mergeSortedArrays(arr1, arr2)
    print(mergedArrays.data)
