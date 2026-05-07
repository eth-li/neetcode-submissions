class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        s = 0
        l = 0
        r = 0

        while r < k:
            s += arr[r]
            r+=1
            print(r)
            print(s)
        if s/k >= threshold:
            total+=1
        
        r-=1
        while r<len(arr)-1:
            r +=1
            s -= arr[l]
            s+= arr[r]
            if s/k >= threshold:
                total+=1
            l+=1
            print("l",l)
            print("r",r)
            print("s",s)
        return total