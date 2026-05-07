class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        s = sum(arr[0:k-1])
        for i in range(len(arr)-k+1):
            s+= arr[i+k-1]
            if s/k >= threshold:
                total+=1
            s -= arr[i]
        return total