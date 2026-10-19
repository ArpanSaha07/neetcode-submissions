class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Time complexity: O(2^(m+n)) 
        # Space complexity: O(m+n), The maximum recursion depth is proportional to m + n, since you can move at most m - 1 steps in one direction and n - 1 in the other before reaching the destination. With a branching factor of 2.

        # def dp(l, b):

        #     if l > m:
        #         return 0

        #     if b > n:
        #         return 0

        #     if l == m and b == n:
        #         return 1
 
        #     return dp(l+1,b) + dp(l,b+1)

        # return dp(1, 1)


        # Time complexity: O(m*n)
        # Space complexity: O(m*n)

        # memo = {}

        # def dp(l, b):

        #     if l > m or b > n:
        #         return 0

        #     if l == m and b == n:
        #         return 1
 
        #     if (l,b) not in memo:
        #         memo[(l,b)] = dp(l+1,b) + dp(l,b+1)

        #     return memo[(l,b)]

        # return dp(1, 1)
        

        
        # bottom-up approach
        # Time complexity: O(m*n)
        # Space complexity: O(m*n)

        # dp = [[0] * n for _ in range(m)]

        # dp[m-1][n-1] = 1

        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):

        #         if i + 1 < m:
        #             dp[i][j] += dp[i+1][j]
                
        #         if j + 1 < n:
        #             dp[i][j] += dp[i][j+1]

        # return dp[0][0]


        # Time complexity: O(m*n)
        # Space complexity: O(n)

        dp = [0] * n

        dp[n - 1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if j + 1 < n:
                    dp[j] += dp[j + 1]

        return dp[0]
