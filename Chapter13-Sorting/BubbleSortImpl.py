if __name__ == '__main__':
    x = [10, 22, 52, 43, 1, 3, 99, 85, 74, 65]

    def bubbleSort(value):
        if len(value) < 2:
            return value
        for i in range(len(value)-1):
            for j in range(len(value)-1):
                a = value[j]
                b = value[j+1]

                if a > b:
                    value[j] = b
                    value[j + 1] = a
        return value

    print(bubbleSort(x))
