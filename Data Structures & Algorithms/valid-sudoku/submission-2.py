from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Time complexity of the solution: O(n^2)
        # Space complexity: O(n^2), since rows, cols and boxes each store up to n^2 values total.
        # O(n²) + O(n²) + O(n²) = O(n²)

        rows = [set() for _ in range(9)]

        cols = [set() for _ in range(9)]

        boxes = collections.defaultdict(set)


        for r in range(9):
            for c in range(9):

                val = board[r][c]

                if val != '.':
                    if val in rows[r] or val in cols[c] or val in boxes[(r // 3, c // 3)]:
                        return False
                    
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3, c // 3)].add(val)

        return True


        


                





        