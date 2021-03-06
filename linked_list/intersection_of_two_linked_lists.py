# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        pA = headA
        pB = headB

        while pA is not pB:
            if pA is None:
                pA = headB
            else:
                pA = pA.next

            if pB is None:
                pB = headA
            else:
                pB = pB.next

        return pA
