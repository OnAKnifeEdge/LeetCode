from heapq import heappush, heappop, heapify
from collections import defaultdict


class Tweet:
    def __init__(self, timestamp, tweet_id, next=None):
        self.timestamp = timestamp
        self.tweet_id = tweet_id
        self.next = next

    def __lt__(self, other):
        return self.timestamp > other.timestamp


class Twitter:
    """
    你把一个用户发布的所有推文做成一条有序链表（靠近头部的推文是最近发布的），
    那么只要合并关注用户的推文链表，即可获得按照时间线顺序排序的信息流。
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # This will hold a linkedlist of tweets for each user
        self.tweets = {}  # user: Tweet
        # This will hold a set of users that each user is following
        self.followees = defaultdict(set)
        self.timestamp = 0  # This is used to order the tweets by time

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        # Append the (time, tweetId) tuple to the list of tweets of userId
        tweet = Tweet(self.timestamp, tweetId, next=self.tweets.get(userId))
        self.tweets[userId] = tweet
        self.timestamp += 1

    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user followed
        or by the user herself.
        Tweets must be ordered from most recent to least recent.
        """
        heap = []
        people = self.followees[userId] | {userId}
        for person in people:
            head = self.tweets.get(person)
            if head:
                heappush(heap, head)

        timeline = []

        while heap and len(timeline) < 10:
            earliest = heappop(heap)

            timeline.append(earliest.tweet_id)

            next_tweet = earliest.next
            if next_tweet:
                heappush(heap, next_tweet)

        return timeline

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee.
        """
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If not a followee, do nothing.
        """
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
