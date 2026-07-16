from collections import Counter, deque


# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
        
#         count = Counter(tasks)

#         # Max heap 
#         maxHeap = [-val for val in count.values()]
#         heapq.heapify(maxHeap)

#         queue = deque()   # [remaining_count, ready_time]
#         time = 0

#         while maxHeap or queue:
#             time += 1

#             if maxHeap:
#                 remaining_count = heapq.heappop(maxHeap) + 1

              
#                 if remaining_count < 0:
#                     queue.append([remaining_count, time + n])
#             else:
                
#                 time = queue[0][1]

            
#             if queue and queue[0][1] == time:
#                 heapq.heappush(maxHeap, queue.popleft()[0])

#         return time 

    
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        ## Create a maxHeap with the frequency of the tasks - since we always want the most frequent task to be prioritised
        count = Counter(tasks)
        maxHeap = [-val for val in count.values()]
        heapq.heapify(maxHeap)

        queue = deque()
        time = 0 
        
        while maxHeap or queue:
            time +=1

            if maxHeap:
                remaining_count = heapq.heappop(maxHeap)+1 ## Since maxheap has neg values - thus to reduce count we do +

                if remaining_count < 0:
                    queue.append(remaining_count, time+n)
            else:
                time = queue[0][1]

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time
