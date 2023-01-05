if __name__ == '__main__':
    def fibonacciRecursive(value):
        if value < 2:
            return value
        return fibonacciRecursive(value-1) + fibonacciRecursive(value-2)

    def fibonacciIterative(value):
        if value < 2:
            return value
        fib = [0, 1]

        for i in range(2, value+1):
            aux = fib[len(fib)-2] + fib[len(fib)-1]
            fib.append(aux)

        index = fib[len(fib)-1]
        return index

    print(fibonacciRecursive(8))
    print(fibonacciIterative(8))