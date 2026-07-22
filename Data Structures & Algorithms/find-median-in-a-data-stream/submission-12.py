class MedianFinder:

    def __init__(self):
        self.lefthp, self.righthp = [], []

    def addNum(self, val: int) -> None:
        print('Adding', val)
        print(self.lefthp, self.righthp)
        if not self.lefthp and not self.righthp:
            self.lefthp.append(-val)
            return
        
        
        if self.lefthp and val > -self.lefthp[0]:
            heapq.heappush(self.righthp, val)
        else:
            heapq.heappush(self.lefthp, -val)
        
        lh, lr = len(self.lefthp), len(self.righthp)
        if abs(lh-lr) > 1:
            if lh>lr:
                heapq.heappush(self.righthp, -heapq.heappop(self.lefthp))
            else:
                heapq.heappush(self.lefthp, -heapq.heappop(self.righthp))
        print('final')
        print(self.lefthp, self.righthp)
        print('**')

    def findMedian(self) -> float:
        lh, lr = len(self.lefthp), len(self.righthp)
        if lh == lr:
            return ((-self.lefthp[0]) + self.righthp[0])/2
        
        if lh>lr:
            return -self.lefthp[0]
        else:
            return self.righthp[0]
        