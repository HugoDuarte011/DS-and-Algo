##What is the Big O of the below function? (Hint, you may want to go line by line)

def anotherFunChallenge(input):
    a = 5
    b = 10
    c = 50
    i, j = 0

    while i < input:
        x = i + 1
        y = i + 2
        z = i + 3

    while j < input:
        p = j * 2
        q = j * 2

    whoAmI = "I don't know"

##Answer: The function has O(n²). Here, we have 2 loops increasing exponentially the runtime of the function.
