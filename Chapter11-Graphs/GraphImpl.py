class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, value = None):
        if value != None:
            self.adjacentList[value] = []
            self.numberOfNodes += 1

    def addEdge(self, x = None, y = None):
        if x != None and y != None:
            self.adjacentList[x].append(y)
            self.adjacentList[y].append(x)

    def showConnections(self):
        allNodes = self.adjacentList.items()
        for node in allNodes:
            nodeConnections = node[1]
            connections = ""
            vertex = None
            for vertex in nodeConnections:
                connections += vertex + " "
            print(node[0] + "-->" + connections)

if __name__ == "__main__":
    print("Hello")

    myGraph = Graph()
    myGraph.addVertex('0')
    myGraph.addVertex('1')
    myGraph.addVertex('2')
    myGraph.addVertex('3')
    myGraph.addVertex('4')
    myGraph.addVertex('5')
    myGraph.addVertex('6')
    myGraph.addEdge('3', '1')
    myGraph.addEdge('3', '4')
    myGraph.addEdge('4', '2')
    myGraph.addEdge('4', '5')
    myGraph.addEdge('1', '2')
    myGraph.addEdge('1', '0')
    myGraph.addEdge('0', '2')
    myGraph.addEdge('6', '5')

    myGraph.showConnections()