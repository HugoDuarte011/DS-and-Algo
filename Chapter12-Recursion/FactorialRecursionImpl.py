if __name__ == '__main__':
    def findFactorialRecursive(value):
        if value <= 2:
            return value
        return value * findFactorialRecursive(value-1)

    def findFactorialIterative(value):
        if value <= 2:
            return value
        answer = value
        for i in range(2, value):
            answer = answer * i
        return answer

    print(findFactorialRecursive(5))
    print(findFactorialIterative(5))