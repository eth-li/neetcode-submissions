class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        res = []
        for num, freq in cnt.most_common(k):
            res.append(num)
        return res


            