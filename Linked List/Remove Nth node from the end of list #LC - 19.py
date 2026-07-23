# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head is None: return head
        prev = None
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        x = count - n
        curr = head
        if x == 0:
            return head.next

        for i in range(1,x + 1):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        return head

## Alternative approach using two pointers
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head is None: return head
        slow = head
        fast = head
        prev = None

        for i in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        prev.next = slow.next
        return head

## A dummy node can also be used to simplify the code and avoid edge cases
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        for i in range(n + 1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next

# Either of the above approaches can be used to remove the Nth node from the end of the linked list. The first approach calculates the length of the list and then removes the Nth node, while the second and third approaches use two pointers to find and remove the Nth node in a single pass.

