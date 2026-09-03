# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # Use a dummy node to handle edge cases where left = 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Step 1: Move `prev` to the node right before the `left` position
        for _ in range(left - 1):
            prev = prev.next
            
        # Step 2: Reverse the sub-list from `left` to `right`
        current = prev.next
        for _ in range(right - left):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
            
        return dummy.next