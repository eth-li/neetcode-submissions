class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        while l < r:
            mid = (l+r)//2
            if target == matrix[mid][0]:
                return True
            elif target > matrix[mid][0]:
                l = mid +1
            else:
                r = mid -1 
        
        if target < matrix[l][0]:
            l -=1

        left = 0
        right = len(matrix[0]) -1
        while left <= right:
            middle = (left+right)//2
            if matrix[l][middle]==target:
                return True
            elif matrix[l][middle] < target:
                left = middle +1
            else:
                right = middle-1
        return False
            