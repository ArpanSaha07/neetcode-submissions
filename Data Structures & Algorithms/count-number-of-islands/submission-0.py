class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Time complexity: O(m*n) because every cell is checked by the nested loops, and each land cell is explored by DFS only once.
        # Space complexity: O(m*n) in the worst case, because the recursive DFS call stack can grow to include every cell in a large island.

        island_count = 0

        def dfs(i,j):

            if grid[i][j] == "1":
                grid[i][j] = "X"
            else:
                return

            if i+1 < len(grid):
                dfs(i+1, j)
            if j+1 < len(grid[0]):
                dfs(i, j+1)
            if i-1 >= 0:
                dfs(i-1, j)
            if j-1 >= 0:
                dfs(i, j-1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == "1":
                    island_count += 1
                    dfs(i, j)

        return island_count

'''
We can use a hash set to track which island cells have been checked without modifying the grid. 

visited = set()

visited.add((0, 0))
visited.add((0, 1))

if (i, j) in visited:
    return

Both insertion and lookup take O(1) average time.
'''






        