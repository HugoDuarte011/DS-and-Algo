if __name__ == '__main__':
    def revertRecursive(value):
        if len(value) < 2:
            return value
        aux = ""
        aux = aux + value[len(value)-1] + revertRecursive(value[:-1])
        return aux

    def revertIterative(value):
        if len(value) < 2:
            return value
        aux = ""
        for i in range(len(value)-1, -1, -1):
            aux = aux + value[i]

        return aux

    print(revertRecursive("Hugo"))
    print(revertIterative("Hugo"))