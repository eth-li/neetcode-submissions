class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        str1 = str()
        str2 = str()
        i=0
        j=len(s)-1
        while j>i:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if s[i] != s[j]:
                return False
            str1 = str1 + s[i]
            str2 = str2 + s[j]
            i+=1
            j-=1
        if str1==str2:
            return True
        return False