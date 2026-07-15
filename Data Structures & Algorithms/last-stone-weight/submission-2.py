# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         stones = [-s for s in stones]
#         heapq.heapify(stones)

#         while len(stones) > 1:
#             p = heapq.heappop(stones)
#             q = heapq.heappop(stones)
#             if q> p:
#                 heapq.heappush(stones, p-q)

#         stones.append(0)
#         return abs(stones[0])


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        ## Create max heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if y> x:
                heapq.heappush(stones, x-y)

        ## Incase all the stones are destroyed
        stones.append(0)
        return abs(stones[0])

        