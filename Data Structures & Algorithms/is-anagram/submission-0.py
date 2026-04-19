class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = tuple(sorted(s))
        m = tuple(sorted(t))
        return n==m