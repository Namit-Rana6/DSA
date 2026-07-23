# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                break
        
        if fast is None or fast.next is None:
            return None
            
        slow = head
        while slow:
            if slow is fast:
                return fast
            slow = slow.next
            fast = fast.next
