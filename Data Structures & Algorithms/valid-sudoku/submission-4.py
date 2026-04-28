class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val==".":
                    continue
                if val in rows[r]:
                    print(val)
                    return False
                if val in cols[c]:
                    print("2")
                    return False
                rows[r].add(val)
                cols[c].add(val)
                key = (r//3,c//3)
                if val in boxes[key]:
                    print("3")
                    return False
                boxes[key].add(val)
        return True
