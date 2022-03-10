# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/?tab=Solutions

# DFS method 1, flip visited node as ocean
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

# DFS method 2, use array to mark visited nodes
class Solution2(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        r, c = len(grid), len(grid[0])
        visited = [[False for _ in range(c)] for _ in range(r)]

        count = 0
        for i in range(r):
            for j in range(c):
                if not visited[i][j] and grid[i][j] == '1':
                    self.dfs(i, j, visited)
                    count += 1
        return count

    def dfs(self, i, j, visited):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0' or visited[i][j]:
            return
        visited[i][j] = True
        self.dfs(i + 1, j, visited)
        self.dfs(i - 1, j, visited)
        self.dfs(i, j + 1, visited)
        self.dfs(i, j - 1, visited)

# BFS method
class Solution3:
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

s1=Solution2()
print("Solution 1 results:")
print(s1.numIslands(grid))

s2=Solution2()
print("Solution 2 results:")
print(s2.numIslands(grid))

s3=Solution3()
print("Solution 3 results:")
print(s3.numIslands(grid))