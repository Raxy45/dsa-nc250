class Twitter:

    def __init__(self):
        self.follower_map = defaultdict(set)
        self.user_tweet_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweet_map[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        # Add current user to its own following list
        # For all user in following list:
        #     Add each users last tweet and the user's next tweet index in max Heap
        
        # Pop out the tweet with highest id from heap -> check if this user has tweet after this by using index
        # if yes -> add that tweet and tweet's index - 1 in heap
        # continue till tweets < 10 or tweet heap exists
        current_user_follower_list = self.follower_map[userId]
        current_user_follower_list.add(userId)

        tweet_list = []
        for user in current_user_follower_list:
            users_tweet_list = self.user_tweet_map[user]
            if users_tweet_list:
                # at least one tweet exists
                users_tweet_count = len(users_tweet_list)
                users_latest_tweet = users_tweet_list[users_tweet_count - 1]
                heapq.heappush(tweet_list, (-users_latest_tweet, user, users_tweet_count - 2))
                # tweet list will contain latest tweet of all the users, which current user follows
        
        ans = []
        while len(ans) < 10 and tweet_list:
            current_tweet, current_user, current_users_old_tweet_index = heapq.heappop(tweet_list)
            ans.append(-current_tweet)
            if current_users_old_tweet_index >=0:
                current_users_old_tweet_id = self.user_tweet_map[current_user][current_users_old_tweet_index]
                heapq.heappush(tweet_list, (-current_users_old_tweet_id, current_user, current_users_old_tweet_index-1))
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follower_map and followeeId in self.follower_map[followerId]:
            self.follower_map[followerId].remove(followeeId)
