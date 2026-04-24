class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new = set(nums)
        new = sorted(new)
        max = 0
        cur = 0
        for num in new:
            print(cur)
            if cur == 0 or num == prev+1 :
                cur +=1
                if cur > max:
                    max = cur
            else:
                if cur > max:
                    max = cur
                cur = 1
            prev = num
        return max