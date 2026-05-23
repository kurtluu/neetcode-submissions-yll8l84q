class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])

        # find the start of island -- searching by '1'
        # bfs/dfs the island -> marking with '#'
        # incr count after
        # return count

        def markIsland(r, c):           
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            if grid[r][c] != '1':
                return
            
            grid[r][c] = '#'
            markIsland(r + 1, c)
            markIsland(r - 1, c)
            markIsland(r, c + 1)
            markIsland(r, c - 1)        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    markIsland(r, c)
                    count += 1
        
        return count
                



