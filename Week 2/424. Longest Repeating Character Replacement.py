class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Use two pointers and dictionaries
        '''
        left = 0
        max_len = 0
        my_counter = {}
        
        
        for right in range(len(s)):
            
            if not s[right] in my_counter:
                my_counter[s[right]] = 0
            my_counter[s[right]] += 1
            
        
            cells_count = right - left + 1
            if cells_count - max(my_counter.values()) <= k:
                max_len = max(max_len, cells_count)
                
            else:
                my_counter[s[left]] -= 1
                if not my_counter[s[left]]:
                    my_counter.pop(s[left])
                left += 1
        
        return max_len
		