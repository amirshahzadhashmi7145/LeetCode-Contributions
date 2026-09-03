class MinStack(object):

    def __init__(self):
     self.stack = []
     self.mins = []
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        if len(self.mins) == 0:
         self.mins.append(value)
        else:
         self.mins.append(min(value, self.mins[-1]))
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.mins.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna