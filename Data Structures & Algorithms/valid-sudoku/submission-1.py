class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #Rows
        for row in board:
            seen= set()
            for col in row:
                if col in seen and not col==".":
                    return False
                seen.add(col)
        
        #Cols
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen and not board[j][i]==".":
                    return False
                seen.add(board[j][i])
        
        #Boxes
        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = set()
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] in seen and not board[i+k][j+l]==".":
                            return False
                        seen.add(board[i+k][j+l])
        return True