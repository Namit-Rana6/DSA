'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        
        slow = head
        fast = head
        
        if head is None or head.next is None:
            return 0
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow is fast:
                break
        
        if fast is None or fast.next is None: return 0
        
        
        count = 1
        slow = slow.next
        while slow is not fast:
            slow = slow.next
            count += 1
        return count
        