class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        my_set=set()
        for i in nums:
            if i in my_set:
                return True
            else:
                my_set.add(i)
        return False