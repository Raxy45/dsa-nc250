class Twitter:

    def __init__(self):
        self.fmp, self.tmp = defaultdict(set), defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tmp[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        total_followers = self.fmp[userId]
        total_followers.add(userId)

        last_tweets_hp = []
        for id in total_followers:
            if self.tmp[id]:
                heapq.heappush(last_tweets_hp, (-self.tmp[id][-1], id, len(self.tmp[id])-2))
        
        ans = []
        while last_tweets_hp and len(ans) < 10:
            current_latest_tweet, uid, tuid = heapq.heappop(last_tweets_hp)
            ans.append(-current_latest_tweet)
            if tuid >= 0:
                heapq.heappush(last_tweets_hp, (-self.tmp[id][tuid], uid, tuid-1))
        return ans
    def follow(self, followerId: int, followeeId: int) -> None:
        self.fmp[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.fmp[followerId]:
            self.fmp[followerId].remove(followeeId)
