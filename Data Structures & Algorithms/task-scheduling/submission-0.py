from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)

        # Max heap (store negative frequencies)
        maxHeap = [-val for val in count.values()]
        heapq.heapify(maxHeap)

        queue = deque()   # [remaining_count, ready_time]
        time = 0

        while maxHeap or queue:
            time += 1

            if maxHeap:
                remaining_count = heapq.heappop(maxHeap) + 1

                # If tasks still remaining (still negative)
                if remaining_count < 0:
                    queue.append([remaining_count, time + n])
            else:
                # Jump time forward if heap empty
                time = queue[0][1]

            # If task cooldown finished
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time
