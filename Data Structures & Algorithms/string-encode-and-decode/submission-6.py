class Solution:

    def encode(self, strs: List[str]) -> str:
        new = str()
        for i in strs:
            length = str(len(i))
            new = new+length+"#"+i
            # print(new)
        return new

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i<len(s):
            j=i
            while j < len(s) and s[j]!="#":
                j+=1
            cur_len = int(s[i:j])
            word = s[j+1:j+cur_len+1]
            res.append(word)
            i=j+1+cur_len
        return res