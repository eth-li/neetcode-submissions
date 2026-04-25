class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for start in range(len(nums)-2):
            target = -nums[start]
            i = start+1
            j = len(nums)-1
            while(i<j):
                s = nums[i]+nums[j]
                if s <target:
                    i+=1
                elif s > target:
                    j-=1
                else:
                    newlist = [nums[start],nums[i],nums[j]]
                    new = tuple(newlist)
                    res.add(new)
                    i+=1
                    j-=1
        return list(res)
                    