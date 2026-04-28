class Solution:

    def encode(self, strs: List[str]) -> str:
        new = str()
        for word in strs:
            length = len(word)
            new = new + str(length) +"#"+ word
        return new

    def decode(self, s: str) -> List[str]:
        res = list()
        i = 0
        while i<len(s):
            j=i
            while not s[j]=="#":
                j+=1
            length = int(s[i:j])
            sub = s[j+1:j+length+1]
            res.append(sub)
            i=j+length+1
        return res

