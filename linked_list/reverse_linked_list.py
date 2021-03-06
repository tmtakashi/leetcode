# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        nextnode = head
        prev = None

        while current:
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode

        return prev
