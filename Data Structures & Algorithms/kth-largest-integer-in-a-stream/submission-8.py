# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k, self.minheap = k, nums
#         heapq.heapify(self.minheap)
        
#         ## Since we always want kth highest number, we can keep size = k
#         while len(self.minheap) > self.k:
#             heapq.heappop(self.minheap)

#     def add(self, val: int) -> int:
#         heapq.heappush(self.minheap, val)
#         if len(self.minheap) > self.k:
#             heapq.heappop(self.minheap)
        
#         return self.minheap[0]

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums, k
        heapq.heapify(self.heap)
        
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self,num):
        heapq.heappush(self.heap,num)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

        

        
