class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])

        def explore(r, c):  
            grid[r][c] = "0"
            if r > 0 and grid[r-1][c] == "1":
                explore(r-1, c)
            if r < rows - 1 and grid[r+1][c] == "1":
                explore(r+1, c)
            if c > 0 and grid[r][c-1] == "1":
                explore(r, c-1)
            if c < cols - 1 and grid[r][c+1] == "1":
                explore(r, c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    explore(r, c)
        
        return count