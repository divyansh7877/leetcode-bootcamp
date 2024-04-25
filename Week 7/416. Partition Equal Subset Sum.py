class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot%2 != 0:
            return False
        target = tot//2

        tracker = set()
        tracker.add(0)

        for num in nums:
            tracker.update([num + curr for curr in tracker])
            if target in tracker:
                return True
        return False