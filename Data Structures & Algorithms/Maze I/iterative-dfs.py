# Stack based iterative DFS solution for the rolling ball maze problem.
# This approach is highly favored in production systems to prevent a StackOverflowError when traversing exceptionally deep graphs or trees.

# Time complexity: O(m*n*(m+n))
# Space complexity: O(m*n)

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
        stack = [(start[0], start[1])]

        while stack:

          i, j = stack.pop()

          if (i, j) in visited:
            continue

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

            if (new_i, new_j) not in visited:
                stack.append(new_i, new_j)

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
