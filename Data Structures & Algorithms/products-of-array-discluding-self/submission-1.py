class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        p=1
        s=1
        for num in nums:
            p=p*num
            pref.append(p)
        suff = []
        for i in reversed(range(len(nums))):
            s = s*nums[i]
            suff.insert(0,s)
        print(pref)
        print(suff)
        res = []
        for i in range(len(nums)):
            if i-1 <0 :
                res.append(suff[1])
            elif i+1==len(nums):
                res.append(pref[len(nums)-2])
            else: res.append(pref[i-1]*suff[i+1])
        return res