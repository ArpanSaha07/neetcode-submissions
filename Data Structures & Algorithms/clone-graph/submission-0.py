"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # Time: O(V + E), because you process every vertex once and traverse its adjacency list.
        # Space: O(V) auxiliary space for the hash map and BFS queue, excluding the cloned graph itself.

        if not node:
            return None

        visited = {}
        visited[node] = Node(node.val)
        queue = deque([node])

        while queue:
            # Remove and return the element from the left side of the queue
            current = queue.popleft()
            
            # Explore all unvisited neighbors of the current node
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                visited[current].neighbors.append(visited[neighbor])
    
        return visited[node]


