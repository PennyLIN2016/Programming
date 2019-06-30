import collections
import heapq
    #Runtime: 84 ms, faster than 66.25% of Python online submissions for Design Twitter.
    #Memory Usage: 18.2 MB, less than 17.65% of Python online submissions for Design Twitter.

class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # count number of tweets
        self.tweet_cnt= 0
        # all tweets in this twitter
        self.tweets= collections.defaultdict(list)
        # all users follow list.
        self.follow_ship = collections.defaultdict(set)


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        # add the tweetId into tweets dict
        # heapq: key = -self.tweet_cnt
        self.tweets[userId].append([-self.tweet_cnt,tweetId])
        self.tweet_cnt+=1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        res=[]
        t_q=[]
        user_list = list(self.follow_ship[userId])+[userId]
        for val in user_list:
            for t in self.tweets[val]:
                heapq.heappush(t_q,t)
        n=0
        while t_q and n<10:
            # add the tweet id into res
            res.append(heapq.heappop(t_q)[1])
            n+=1
        return res




    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            self.follow_ship[followerId].add(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.follow_ship and followeeId in self.follow_ship[followerId]:
            return self.follow_ship[followerId].remove(followeeId)



    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            self.follow_ship[followerId].add(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.follow_ship and followeeId in self.follow_ship[followerId]:
            return self.follow_ship[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
obj = Twitter()
userId= 1
tweetId= 5
followerId=1
followeeId=2
obj.postTweet(userId,tweetId)
param_2 = obj.getNewsFeed(userId)
obj.follow(followerId,followeeId)
obj.unfollow(followerId,followeeId)
