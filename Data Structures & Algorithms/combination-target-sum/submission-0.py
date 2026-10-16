class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        
        # [2, 3], [3, 2]
        # Time complexity: O(N^(T/M)) where `M` is the smallest element in the given list, `T` is the target, and `N` is the number of candidates.
        # What is the deepest length of a tree? O(T/M)
        # how the number of nodes grows as we add another level to the recursion tree = O(N^D), where D: depth
        # Space complexity: O(T/M) + O(T/M) current + result lists = O(T/M)

        result = []

        def backtrack(current, remaining, start):

            if remaining < 0:
                return

            if remaining == 0:
                result.append(current.copy())  # we use current.copy() because the current list will be modified as backtracking continues
                return

            for i in range(start, len(nums)):

                num = nums[i]

                current.append(num)

                backtrack(current, remaining - num, i)

                current.pop()


        backtrack([], target, 0)

        return result



















        


            


        