# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/?tab=Solutions

# DFS method
class Solution1:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid)
                    res += 1
        return res

    def dfs(self, i, j, grid):
        grid[i][j] = '0'

        if i + 1 < len(grid) and grid[i + 1][j] == '1':
            self.dfs(i + 1, j, grid)

        if j + 1 < len(grid[0]) and grid[i][j + 1] == '1':
            self.dfs(i, j + 1, grid)

        if i - 1 >= 0 and grid[i - 1][j] == '1':
            self.dfs(i - 1, j, grid)

        if j - 1 >= 0 and grid[i][j - 1] == '1':
            self.dfs(i, j - 1, grid)

# BFS method
class Solution2:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        res = 0
        queue = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    queue.append([i, j])
                    grid[i][j] = '0'
                    while queue:
                        [a, b] = queue.pop(0)

                        if a + 1 < m and grid[a + 1][b] == '1':
                            queue.append([a + 1, b])
                            grid[a + 1][b] = '0'

                        if b + 1 < n and grid[a][b + 1] == '1':
                            queue.append([a, b + 1])
                            grid[a][b + 1] = '0'

                        if a - 1 >= 0 and grid[a - 1][b] == '1':
                            queue.append([a - 1, b])
                            grid[a - 1][b] = '0'

                        if b - 1 >= 0 and grid[a][b - 1] == '1':
                            queue.append([a, b - 1])
                            grid[a][b - 1] = '0'

                    res += 1
        return res

grid=[['0','0','0','1','0','0','0','0'],['0','0','1','1','1','0','0','1'],['0','0','0','1','1','0','1','0'],['0','0','1','1','1','0','0','0']]
a=Solution1()
print a.numIslands(grid)