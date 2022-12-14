## What is the Big O of the below function? (Hint, you may want to go line by line)

def funChallenge(input):
    a = 10
    a = 50 + 3

    i = 0

    for i in range(len(input)):
        anotherFunction()
        stranger = True
        a += 1
    return a

def anotherFunction():
    return 0

##Answer: The function has O(n), because the complexity deppends on the quantity of elements in the input object.