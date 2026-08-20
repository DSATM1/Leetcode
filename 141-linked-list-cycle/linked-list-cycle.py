class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # Move 1 step
            fast = fast.next.next     # Move 2 steps
            
            if slow == fast:          # Cycle detected
                return True
                
        return False                  # Reached end of list (no cycle)