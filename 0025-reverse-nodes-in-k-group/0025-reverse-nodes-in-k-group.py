class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def get_kth_node(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        
        def reverse_linked_list(head, k):
            new_head, ptr = None, head
            while k > 0:
                next_node = ptr.next
                ptr.next = new_head
                new_head = ptr
                ptr = next_node
                k -= 1
            return new_head
        
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            kth = get_kth_node(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            
            # Reverse the group
            prev, curr = group_next, group_prev.next
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = group_prev.next
            group_prev.next = prev
            group_prev = tmp
        
        return dummy.next
        