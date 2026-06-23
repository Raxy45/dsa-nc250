class MedianFinder:

    def __init__(self):
        self.lhs, self.rhs = [], []

    def addNum(self, num: int) -> None:
        if not self.lhs and not self.rhs:
            self.lhs.append(-num)
            return
        
        if num <= abs(self.lhs[0]):
            heapq.heappush(self.lhs, -num)
        else:
            heapq.heappush(self.rhs, num)
        
        if abs(len(self.lhs) - len(self.rhs)) >1:
            if len(self.lhs) > len(self.rhs):
                heapq.heappush(self.rhs, -heapq.heappop(self.lhs))
            else:
                heapq.heappush(self.lhs, -heapq.heappop(self.rhs))
        print('after adding num', num)
        print(self.lhs, self.rhs)

    def findMedian(self) -> float:
        print('finding median for', self.lhs, self.rhs)
        if (len(self.lhs) + len(self.rhs))%2 == 0:
            print('even length')
            return (-self.lhs[0]+self.rhs[0])/2
        else:
            if len(self.lhs)>len(self.rhs):
                return -self.lhs[0]
            else:
                return self.rhs[0]
        