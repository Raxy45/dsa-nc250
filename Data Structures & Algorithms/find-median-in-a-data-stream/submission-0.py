class MedianFinder:

    def __init__(self):
        self.hp, self.median = [], 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.hp, num)
        length = len(self.hp)
        mid = length // 2
        if length%2>0:
            self.median = self.hp[mid]
        else:
            self.median = (self.hp[mid] + self.hp[mid-1])/2


    def findMedian(self) -> float:
        return self.median
        