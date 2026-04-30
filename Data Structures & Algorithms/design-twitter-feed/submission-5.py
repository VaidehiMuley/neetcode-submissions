class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:

        self.tweetMap[userId].append([self.count ,tweetId])
        self.count -=1

    def getNewsFeed(self, userId: int) -> List[int]:

        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        ## Loop through all the ppl user follows to get latest tweets
        for followee in self.followMap[userId]:
            ## Check if the followee has made any tweets
            if followee in self.tweetMap:
                ## Get the latest tweet that the followee has made
                index = len(self.tweetMap[followee])-1
                count, tweetId = self.tweetMap[followee][index]
                minHeap.append([count, tweetId,followee,index -1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId,followee,index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followee][index]
                index -=1
                heapq.heappush(minHeap, [count,tweetId,followee,index])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


        
