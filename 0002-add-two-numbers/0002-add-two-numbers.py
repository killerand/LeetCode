# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        added = ListNode()
        current_node = added
        carry_over = 0

        while l1 or l2 or carry_over:
            sum_val = carry_over
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            
            current_node.next = ListNode(val=sum_val % 10)
            carry_over = sum_val // 10
            current_node = current_node.next
        
        return added.next


       
        