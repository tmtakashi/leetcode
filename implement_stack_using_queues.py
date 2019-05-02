# https://leetcode.com/problems/implement-stack-using-queues/


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.q1:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            output = self.q1.pop()
            while self.q2:
                self.q1.append(self.q2.pop(0))
            return output
        return None

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q1[len(self.q1) - 1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """

        return self.q1 == []


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
