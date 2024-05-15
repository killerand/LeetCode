# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node which acts as a new head node that points to the current head
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers, both pointing to the dummy node initially
        first = dummy
        second = dummy
        
        # Move the first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until the first pointer reaches the end of the list
        while first is not None:
            first = first.next
            second = second.next
        
        # The second pointer is now just before the node to be deleted
        second.next = second.next.next
        
        # Return the head of the modified list
        return dummy.next
