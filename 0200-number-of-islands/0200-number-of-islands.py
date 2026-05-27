class Solution:
    def numIslands(self, grid):
        
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        def dfs(r, c):

            # Out of bounds OR water
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] == "0"
            ):
                return

            # Mark visited land as water
            grid[r][c] = "0"

            # Visit all 4 directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        for r in range(rows):
            for c in range(cols):

                # Found new island
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands