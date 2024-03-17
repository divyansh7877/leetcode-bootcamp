class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Use two pointers, one moves at the double step compared to the first pointer head. If the double pointer reaches the end, ie the single pointer has only moved half the steps.
        '''
        single_p = head
        double_p = head

        while double_p and double_p.next:
            single_p=single_p.next
            double_p=double_p.next.next
        
        return single_p
