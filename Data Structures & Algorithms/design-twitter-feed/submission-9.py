class Twitter:

    def __init__(self):
        self.follower_map = defaultdict(set)
        self.tweet_map = defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append(-tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.tweet_map: return []
        current_uid_follower = self.follower_map[userId]
        current_uid_follower.add(userId)
        temp_tweets = []
        for uid in list(current_uid_follower):
            if uid in self.tweet_map:
                temp_tweets.append((self.tweet_map[uid][-1], uid, -2))
        heapq.heapify(temp_tweets)
        tweets = []
        print(temp_tweets)
        while temp_tweets and len(tweets)<10:
            print('inn')
            latest_tweet, uid, idx = heapq.heappop(temp_tweets)
            tweets.append(-latest_tweet)
            print(idx)
            if abs(idx)<len(self.tweet_map[uid]):
                heapq.heappush(temp_tweets, (self.tweet_map[uid][-idx], idx+1))
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].remove(followeeId)
