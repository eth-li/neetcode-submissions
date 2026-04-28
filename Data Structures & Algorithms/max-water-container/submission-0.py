class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        res = 0
        while i < j:
            l = heights[i]
            r= heights[j]
            w = j-i
            h = min(l,r)
            res = max(w*h, res)
            if l <= r:
                i+=1
            else: j-=1
        return res
