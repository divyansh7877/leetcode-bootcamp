class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        '''
        Problem Link: https://leetcode.com/problems/contains-duplicate/description/
        Solved using data structure sets. Can also use dictionaries, or hashmaps.
        '''
        my_set=set()
        for i in nums:
            if i in my_set:
                return True
            else:
                my_set.add(i)
        return False