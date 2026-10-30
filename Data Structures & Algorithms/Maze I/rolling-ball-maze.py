# NOTE: Rolling baLL maze problem.

# Time complexity: O(m*n*(m+n)) Each cell is visited at most once, and for each cell, we may traverse in all four directions until hitting a wall.
# Space complexity: O(m*n) visited set and recursive call stack


# "I'm using DFS to explore the maze. Unlike a normal maze problem, the ball keeps moving until it hits a wall. 
# So for each stopping position, I simulate rolling in all four directions. I then recursively explore each resulting stopping position, 
# tracking visited positions to avoid cycles. If any DFS call reaches the destination, I return true."


class Solution:
    def hasPath(
        self,
        maze: List[List[int]],
        start: List[int],
        destination: List[int]
    ) -> bool:
        # Write your solution here

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Down, Right, Up, Left
        visited = set()  # To keep track of visited positions

        def dfs(i, j):

          if (i, j) in visited:
             return False
             
          if i == destination[0] and j == destination[1]:
            return True

          visited.add((i, j))

          for di, dj in directions:

            new_i, new_j = i, j

            while (
              0 <= new_i + di < len(maze)
              and 0 <= new_j + dj < len(maze[0])
              and maze[new_i + di][new_j + dj] == 0
            ):
              new_i += di
              new_j += dj

            # DFS only after the ball stops
            if dfs(new_i, new_j):
              return True
             
          return False

if __name__ == "__main__":
    # Example usage
    maze = [[0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]]
    
    maze2 = [[0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0],
                [1, 1, 0, 1, 1],
                [0, 0, 0, 1, 0]]
    start = [0, 4]
    destination = [4, 4]
    
    solution = Solution()
    result = solution.hasPath(maze, start, destination)
    print(result)  # Output: True or False based on the maze configuration

    print("Testing second maze configuration:")
    result2 = solution.hasPath(maze2, start, destination)
    print(result2)  # Output: True or False based on the second maze configuration

        return dfs(start[0], start[1])
