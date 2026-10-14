class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j].isnumeric():
                    dig = board[i][j]
                    
                    if dig in rows[i]:
                        return False
                    elif dig in cols[j]:
                        return False
                    elif dig in boxes[(i // 3) * 3 + (j // 3)]:
                        return False

                    rows[i].add(dig)
                    cols[j].add(dig)
                    boxes[(i // 3) * 3 + (j // 3)].add(dig)
        
        return True