# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            # Find the k-th node to see if we have a full group to reverse
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            
            # Reverse the current group
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                
            # Update pointers to connect the reversed group to the rest of the list
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            
        return dummy.next
    
    def getKth(self, curr: ListNode | None, k: int) -> ListNode | None:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr