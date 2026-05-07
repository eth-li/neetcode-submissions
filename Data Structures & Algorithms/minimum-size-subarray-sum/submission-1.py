class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l =0
        length = len(nums)+1

        for r in range(len(nums)):
            while sum(nums[l:r+1]) >= target:
                length = min(length, r-l+1)
                l+=1
        if length== len(nums)+1:
            return 0
        return length
