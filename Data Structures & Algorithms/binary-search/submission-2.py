class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)-1
        mid = r//2
        while not nums[mid] == target and not mid==l and not mid == r:
            if nums[mid] > target:
                r = mid
            else:
                l = mid
            mid = (r+l)//2
        if nums[mid] == target:
            return mid
        elif nums[r] == target:
            return r
        else:
            return -1