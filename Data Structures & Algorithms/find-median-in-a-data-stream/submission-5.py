class MedianFinder:

    def __init__(self):
        self.min_hp, self.max_hp = [], []
        self.len = 0

    def addNum(self, num: int) -> None:
        if not self.min_hp and not self.max_hp:
            heapq.heappush(self.max_hp, -num)
            return
        
        if num > abs(self.max_hp[0]):
            heapq.heappush(self.min_hp, num)
        else:
            heapq.heappush(self.max_hp, -num)
        
        if abs(len(self.max_hp) - len(self.min_hp)) > 1:
            if len(self.max_hp) > len(self.min_hp):
                heapq.heappush(self.min_hp, -heapq.heappop(self.max_hp))
            else:
                heapq.heappush(self.max_hp, -heapq.heappop(self.min_hp))
        print(num, self.max_hp, self.min_hp)

    def findMedian(self) -> float:
        if (len(self.max_hp) + len(self.min_hp))%2 > 0:
            if len(self.max_hp) > len(self.min_hp):
                return -self.max_hp[0]
            else:
                return self.min_hp[0]
        return (-self.max_hp[0] + self.min_hp[0])/2
        