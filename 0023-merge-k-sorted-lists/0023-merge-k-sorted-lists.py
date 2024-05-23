from heapq import heappush, heappop
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    # To ensure that ListNode can be compared in the heap
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        # Initialize the heap with the head nodes of each list
        for idx, node in enumerate(lists):
            if node:
                heappush(min_heap, (node.val, idx, node))
        
        # Dummy head for the result list
        dummy = ListNode()
        current = dummy
        
        # Extract the smallest element from the heap and add it to the result list
        while min_heap:
            val, idx, node = heappop(min_heap)
            current.next = node
            current = current.next
            
            # If the extracted node has a next node, push it into the heap
            if node.next:
                heappush(min_heap, (node.next.val, idx, node.next))
        
        return dummy.next
    
        