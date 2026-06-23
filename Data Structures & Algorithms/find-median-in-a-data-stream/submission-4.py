class MedianFinder:

    def __init__(self):
        self.minHp, self.maxHp = [], []
        self.median = 0

    def addNum(self, num: int) -> None:
        if len(self.minHp) == len(self.maxHp) == 0:
            heapq.heappush(self.minHp, num)
            self.median = num
            return
        
        if self.minHp and num <= self.minHp[0]:
            heapq.heappush(self.maxHp, -num)
        else:
            heapq.heappush(self.minHp, num)

        while abs(len(self.maxHp) - len(self.minHp)) > 1:
            if len(self.minHp) > len(self.maxHp):
                popped = heapq.heappop(self.minHp)
                heapq.heappush(self.maxHp, -popped)
            else:
                popped = heapq.heappop(self.maxHp)
                heapq.heappush(self.minHp, -popped)
            
        
    def findMedian(self) -> float:
        if len(self.minHp) > len(self.maxHp):
            return self.minHp[0]
        elif len(self.maxHp) > len(self.minHp):
            return -self.maxHp[0]
        else:
            return (-self.maxHp[0] + self.minHp[0]) / 2
        