class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Time complexity: O(nlogn)
        # Space: O(n)

        self.heap = stones[:]

        heapq.heapify_max(self.heap)     # O(n)

        while len(self.heap) > 1: # Repeat at most n − 1 times

            max_element = heapq._heappop_max(self.heap) # O(log n)

            second_max = heapq._heappop_max(self.heap) # O(log n)

            diff = max_element - second_max

            if diff > 0:
                heapq._heappush_max(self.heap, diff) # O(log n)

        return self.heap[0] if self.heap else 0


        

        






        