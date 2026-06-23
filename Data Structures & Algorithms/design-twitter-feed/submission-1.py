class Twitter:

    def __init__(self):
        self.count = 0
        self.followersMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        min_heap = []
        self.followerMap[userId].add(userId)
        for follower in self.followerMap[userId]:
            if follower in self.tweetMap: # if he has tweeted anything only then add
                index = len(self.tweetMap[userId]) - 1 
                # This index will point to the current tweet from the user which was popped out
                count, tweetId = self.tweetMap[follower][index]

                # index -1 will always point to the next last tweet from the follower
                heapq.heappush(min_heap, [count, tweetId, follower, index-1])
        
        while min_heap and len(res) < 10:
            count, tweetId, follower, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[follower][index]
                heapq.heappush(min_heap, [count, tweetId, follower, index-1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followersMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followersMap[followerId].remove(followeeId)
