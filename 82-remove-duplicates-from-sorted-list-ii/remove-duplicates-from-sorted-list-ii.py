# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node points to the head to handle cases where the head itself is a duplicate
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        
        while curr:
            # If we detect a duplicate
            if curr.next and curr.val == curr.next.val:
                # Move current pointer to the last node of these duplicates
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Skip all the duplicates by pointing prev's next to curr's next
                prev.next = curr.next
            else:
                # If no duplicate, just move the prev pointer forward
                prev = prev.next
            
            # Move current pointer forward for the next iteration
            curr = curr.next
            
        return dummy.next