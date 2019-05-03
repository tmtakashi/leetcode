# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        right_node = left_node = head

        while right_node and right_node.next:
            right_node = right_node.next.next  # moves 2 times faster than left_node
            left_node = left_node.next

        # reverse the second half linked list
        rev_node = None
        while left_node:
            nxt = left_node.next
            left_node.next = rev_node
            rev_node = left_node
            left_node = nxt

        # compare reversed second half with first half
        while rev_node:
            if rev_node.val != head.val:
                return False
            rev_node = rev_node.next
            head = head.next

        return True
