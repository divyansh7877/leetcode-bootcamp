# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        Count length.
        And reverse the k group over and over again.
        '''
        length = 0
        current_node = head
        
        while current_node and length < k:
            current_node = current_node.next
            length += 1
        
        if length < k:
            return head

        previous_node = None
        current_node = head
        iter=0
        
        while iter<k:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            iter+=1
        
        head.next = self.reverseKGroup(current_node, k)
        
        return previous_node