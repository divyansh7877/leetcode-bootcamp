class Solution:
    def dfs(self, matrix, start, dp):
        i = start[0]
        j = start[1]
        rows = len(matrix)
        cols = len(matrix[0])
        if(dp[i][j]):
            return dp[i][j]

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        path = 1

        for d in directions:
            nx = i+d[0]
            ny = j+d[1]

            if(0<= nx <rows and 0<= ny < cols and matrix[nx][ny] > matrix[i][j]):
                path = max(path, 1 + self.dfs(matrix, (nx, ny), dp))
            
        dp[i][j] = path
        return path
    

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows,cols = len(matrix),len(matrix[0])

        dp = [[0]*cols for i in range(rows)]  # 0 grid

        res = []
        for i in range(rows):
            for j in range(cols):
                ans = self.dfs(matrix, (i,j), dp)
                res.append(ans)

        return max(res)