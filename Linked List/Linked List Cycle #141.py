# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None or head.next.next is None:
            return False
        T = head
        H = head
        while H and H.next:
            T = T.next
            H = H.next.next

            if T is H:
                return True
        return False
