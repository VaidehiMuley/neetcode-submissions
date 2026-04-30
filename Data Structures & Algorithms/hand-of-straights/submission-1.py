class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)% groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1+ count.get(n,0)

        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for i in range(first, first+groupSize):
                # Check if the minimum element of hand is in count
                if i not in count:
                    return False
                count[i] -=1
                # If the count of this element is 0, then pop from heap   
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True

        