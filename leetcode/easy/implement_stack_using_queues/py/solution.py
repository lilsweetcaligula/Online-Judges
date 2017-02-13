import collections

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = collections.deque()


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self._queue.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        tempQueue = collections.deque()
        
        while len(self._queue) > 1:
            x = self._queue.popleft()
            tempQueue.append(x)
            
        result = self._queue.pop()
        
        while len(tempQueue) > 0:
            x = tempQueue.popleft()
            self._queue.append(x)
            
        return result
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        result = self.pop()
        
        self._queue.append(result)
        
        return result
        
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self._queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
