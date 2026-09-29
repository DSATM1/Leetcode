# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # Create a dummy node to handle edge cases like removing the head itself
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # Move the fast pointer n + 1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both pointers at the same speed until fast reaches the end
        while fast is not None:
            fast = fast.next
            slow = slow.next
            
        # slow is now just before the node we want to delete
        slow.next = slow.next.next
        
        return dummy.next