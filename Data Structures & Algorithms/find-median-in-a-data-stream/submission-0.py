class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        # By default add to min heap
        heapq.heappush(small, -1 * num) # Since max heap, hence * -1
        if (self.small) and (self.large) and (abs(self.small[0]) > self.large[0]):
            large_val = abs(heapq.heappop(self.small))
            heapq.heappush(self.large, large_val)

        ## Make sure diff <= 1
        if len(self.small) > len(self.large)+1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)

        elif len(self.small) < len(self.large)+2:
            val = heapq.heappop(self.large)
            heapq.heappush(self.large, abs(val))

    def findMedian(self) -> float:
        if len(self.small) != len(self.large):
            ## Odd number of elements
            if len(self.small) > len(self.large):
                return -1 * self.small[0]
            else:
                return self.large[0]
        else:
            return (abs(self.small[0]) + self.large[0])//2
        
        