class Twitter:

    def __init__(self):
        self.tm, self.fm = defaultdict(list), defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tm[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        print('UserId', userId)
        # 1. get all person who the user is following from dict
        # 2. add current user id to the list
        # 3. create temporary tweet list of all the tweets of all the users present in above list
        # 4. do heapify, pop out the last 10 tweets and return the answer

        # App 2:
        # 1. get all person who the user is following from dict
        # 2. add current user id to the list
        # 3. now, fetch last tweet of all the users add to temporary tweet list(hp)
        # 4. now, pop the latest one -> add to answer arr. if the given user has more tweets. add the next tweet
        # of that user to heap. 
        # 5. repeat step 4, until ans>10 or tweet list is exhausted
        # if userId not in self.tm: return []
        following_list = self.fm[userId].copy()
        following_list.add(userId)

        hp = []
        print('followers are', following_list)
        for user in following_list:
            if user not in self.tm: continue
            hp.append((-self.tm[user][-1], user, -2))
        print('latest tweet of all followers are', hp) # Has list of last tweet of all user in format (-tweetId, userId)

        ans = []
        heapq.heapify(hp)
        while len(ans)<10 and hp:
            # when we have 10 tweets, we can exit
            # when the tweets are exhausted, we can exit
            tweet, userId, tweet_index_for_user = heapq.heappop(hp)
            ans.append(-tweet)
            if abs(tweet_index_for_user) > len(self.tm[userId]):
                # This means, we have added all the tweets from the user
                continue
            
            # now add the latest - 1 tweet of the user
            heapq.heappush(hp, (-self.tm[userId][tweet_index_for_user], userId, tweet_index_for_user-1))
        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        self.fm[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.fm:
            if followeeId in self.fm[followerId]:
                self.fm[followerId].remove(followeeId)
