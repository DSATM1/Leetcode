class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Dummy nodes to start the two separate lists
        before_dummy = ListNode(0)
        before = before_dummy
        after_dummy = ListNode(0)
        after = after_dummy
        
        # Traverse the original list
        current = head
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next
            
        # Ensure the last node of the 'after' list points to None to prevent cycles
        after.next = None
        
        # Connect the 'before' list to the 'after' list
        before.next = after_dummy.next
        
        return before_dummy.next