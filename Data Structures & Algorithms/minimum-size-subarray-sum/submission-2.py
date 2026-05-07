class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l =0
        length = len(nums)+1

        s=0
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                length = min(length, r-l+1)
                s-=nums[l]
                l+=1
        if length== len(nums)+1:
            return 0
        return length
