class MyQueue(object):

    def __init__(self, value=None):
        if value == None:
            self.mQ = []
        else:
            self.mQ = []
            self.mQ.append(value)

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if type(self.mQ) != type([]):
            self.mQ = []
        self.mQ.insert(0, x)
        return None

    def pop(self):
        """
        :rtype: int
        """
        return self.mQ.pop()

    def peek(self):
        """
        :rtype: int
        """
        if type(self.mQ) != type([]):
            return 0
        return self.mQ[len(self.mQ) - 1]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.mQ) <= 0:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()