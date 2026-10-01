# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        # Base cases: empty list, single node, or no rotation needed
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find the length of the list and the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # Step 2: Optimize k
        k = k % length
        if k == 0:
            return head
            
        # Step 3: Find the new tail (length - k - 1 steps from the head)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
            
        # Step 4: Perform the rotation
        new_head = new_tail.next
        new_tail.next = None  # Break the connection
        tail.next = head      # Connect old tail to the old head
        
        return new_head