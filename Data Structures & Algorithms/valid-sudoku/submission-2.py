class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_seen = defaultdict(set)
        cols_seen = defaultdict(set)
        boxes_seen = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val==".":
                    continue
                box_idx = (r//3)+(c//3)*3
                if val in rows_seen[r] or val in cols_seen[c] or val in boxes_seen[box_idx]:
                    return False
                rows_seen[r].add(val)
                cols_seen[c].add(val)
                boxes_seen[box_idx].add(val)
        return True