class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to help with edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize pointers
        prev = dummy
        
        # Iterate through the list in pairs
        while head and head.next:
            # Nodes to be swapped
            first = head
            second = head.next
            
            # Swapping logic
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Re-position pointers for next swap
            prev = first
            head = first.next
        
        # Return the new head, which is the next of the dummy node
        return dummy.next
        