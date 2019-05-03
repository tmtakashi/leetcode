# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if self.s1:
            while self.s1:
                self.s2.append(self.s1.pop())
            self.s1.append(x)

            while self.s2:
                self.s1.append(self.s2.pop())
        else:
            self.s1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.s1.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.s1:
            return self.s1[len(self.s1) - 1]

        return None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """

        return self.s1 == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
