class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        # "I'll use Python's built-in min-heap implementation. I'll maintain a heap of size k so that the root always represents the kth largest element."

        # Overall: O(n + (n-k) log n) when n > k, and O(n) otherwise.
        # Space complexity: O(n) for the copied list, which eventually shrinks to O(k).

        self.k = k
        self.heap = nums[:]

        heapq.heapify(self.heap)  # min heap, so first index will have the lowest value, time complexity: O(n)

        # Remove elements until heap size <= k

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)  #  O(log n)


    def add(self, val: int) -> int:  # O(log k), heap space O(k)
        heapq.heappush(self.heap, val)  # O(log k)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)   # O(log k)

        return self.heap[0]


'''
Why O(log k)?
A heap is a complete binary tree, meaning its height grows logarithmically with the number of elements.
- heappush() may move an element from a leaf to the root: O(log k).
- heappop() may move an element from the root toward a leaf: O(log k).
- Returning the root takes O(1).
'''        



'''
import heapq

nums = [5, 3, 8, 1, 2]

heapq.heapify(nums)       # O(n)
heapq.heappush(nums, 4)   # O(log n)
heapq.heappop(nums)       # O(log n)  deleting


'''