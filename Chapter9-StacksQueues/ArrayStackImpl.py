class MyArrayStack:
    def __init__(self, value):
        self = []
        self.append(value)
        ##self.length = 1

    def pop(self):
        val = self.data[self.lenght-1]
        del self.data[self.lenght-1]
        self.lenght -= 1
        return val

    def append(self, item):
        self.data[self.lenght] = item
        self.lenght+=1
        return self.data

    def peek(self):
        return self[len(self)]
class LessonArrayStack:

    def __init__(self, value = None):
        if value != None:
            self.array = [value]
        else:
            self.array = []

    def peek(self):
        return self.array[len(self.array)-1]

if __name__ == '__main__':

    # myArrayStack = MyArrayStack(10)
    # print(myArrayStack)
    # myArrayStack.append(12)
    # print(myArrayStack)
    # myArrayStack.append(16)
    # print(myArrayStack)
    # myArrayStack.pop()
    # print(myArrayStack)
    # print(myArrayStack.peek())

    lessonArrayStack = LessonArrayStack(5)
    print(lessonArrayStack.array)
    lessonArrayStack.array.append(10)
    print(lessonArrayStack.array)
    lessonArrayStack.array.append(12)
    print(lessonArrayStack.array)
    lessonArrayStack.array.append(16)
    print(lessonArrayStack.array)
    lessonArrayStack.array.pop()
    print(lessonArrayStack.array)
    print(lessonArrayStack.peek())
    print(lessonArrayStack.array)




