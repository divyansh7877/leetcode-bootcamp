class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minimum = min(nums) # Min Value
        maximum = max(nums) # Max Value

        res = [0] * (maximum - minimum + 1)

        for num in nums:
            res[num - minimum] += 1
        
        k_temp = 0
        for i in range(len(res)-1, -1, -1):   # Move from End to start
            k_temp += res[i]
            if k_temp >= k:
                return i + minimum