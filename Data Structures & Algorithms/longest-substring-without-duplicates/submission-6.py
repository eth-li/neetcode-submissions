class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        seen = set()
        end = 0
        while end < len(s):
            if s[end] in seen:
                max_len = max(len(seen),max_len)
                seen.remove(s[start])
                start +=1
            else:
                seen.add(s[end])
                end+=1
        max_len = max(len(seen),max_len)
        return max_len
        