class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])

        # search through grid finding for start of islands
        # dfs through and mark with '#'
        # incr islands
        # repeat

        def dfs(r, c):
            # base case
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1":                
                return 

            if grid[r][c] == "1":
                grid[r][c] = '#'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands
