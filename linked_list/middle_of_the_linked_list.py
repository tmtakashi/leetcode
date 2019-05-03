# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head.next is None:
            return head

        if head.next.next is None:
            return head.next

        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
