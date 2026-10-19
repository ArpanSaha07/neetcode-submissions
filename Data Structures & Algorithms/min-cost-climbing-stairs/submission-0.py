class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # Time complexity: O(n), Exponential O(2^n) without memoization
        # Space complexity: O(n)
        # Because the max length of the memo dictionary is O(n) and, the longest regressive path is n + 1, the maximum recursion depth is n + 1, therefore the recursion stack uses O(n) space. 


        # Approach 1: acculmulate cost

        # def dfs(i, c):

        #     if i>=len(cost):
        #         return c

        #     if i>=0:
        #         c += cost[i]

        #     return min(dfs(i+1,c), dfs(i+2, c))

        # return dfs(-1, 0)

        # Approach 2: return the min remaining cost

        # def dfs(i): # minimum cost to reach the top from index i
        #     if i >= len(cost):
        #         return 0

        #     return cost[i] + min(dfs(i + 1), dfs(i + 2))

        # return min(dfs(0), dfs(1))

        memo = {}

        def dfs(i): # minimum cost to reach the top from index i
            if i >= len(cost):
                return 0

            if i not in memo:
                memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return memo[i]

        return min(dfs(0), dfs(1))


        



        