
import heapq
class Twitter:

    def __init__(self):
        self.users = {}
        self.time = 0
        
    def _incr_time(self):
        self.time += 1
    
    def _init_user(self, userId: int):
        self.users[userId] = {
            'posts': [],
            'following': set()
        }

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._incr_time()
        if userId not in self.users:
            self._init_user(userId)
        
        heapq.heappush_max(self.users[userId]['posts'], (self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # user feed
        feed = heapq.nlargest(10, self.users[userId]['posts'])
        for follower in self.users[userId]['following']:
            feed += heapq.nlargest(10, self.users[follower]['posts'])
        
        heapq.heapify_max(feed)
        return [t for _, t in heapq.nlargest(10, feed)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self._init_user(followerId)
    
        if followerId != followeeId:
            self.users[followerId]['following'].add(followeeId)



    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId]['following'].discard(followeeId)