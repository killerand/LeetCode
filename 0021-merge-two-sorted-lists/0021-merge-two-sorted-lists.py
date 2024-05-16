# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode(0)
        # Create a pointer to track the current node in the merged list
        current = dummy
        
        # While both lists are not empty
        while l1 and l2:
            # Compare the values of the nodes from both lists
            if l1.val < l2.val:
                # Append the node from the first list to the merged list
                current.next = l1
                l1 = l1.next
            else:
                # Append the node from the second list to the merged list
                current.next = l2
                l2 = l2.next
            # Move the pointer to the next node in the merged list
            current = current.next
        
        # If any list still has remaining nodes, append them to the merged list
        current.next = l1 if l1 else l2
        
        # Return the head of the merged list (excluding the dummy node)
        return dummy.next