class MyQueue(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack = []    


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self._stack.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        tempStack = []
        
        while len(self._stack) > 1:
            x = self._stack.pop()
            tempStack.append(x)
        
        result = self._stack.pop()
        
        while len(tempStack) > 0:
            x = tempStack.pop()
            self._stack.append(x)
            
        return result


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        tempStack = []
        
        while len(self._stack) > 0:
            x = self._stack.pop()
            tempStack.append(x)
        
        result = tempStack[-1]
        
        while len(tempStack) > 0:
            x = tempStack.pop()
            self._stack.append(x)
            
        return result


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self._stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
