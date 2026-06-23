class MedianFinder:

    def __init__(self):
        self.lhs, self.rhs = [], []
        self.total_len = 0
        

    def addNum(self, num: int) -> None:
        print('NUM', num)
        print('before adding heap is', self.lhs, self.rhs)
        if not self.lhs and not self.rhs:
            print('first element, added to self.rhs')
            heapq.heappush(self.rhs, num)
            return

        if num < -self.rhs[0]:
            heapq.heappush(self.lhs, -num)
        else:
            heapq.heappush(self.rhs, num)
    
        print('after adding', self.lhs, self.rhs)
        while abs(len(self.lhs) - len(self.rhs)) >1:
            print('HEAPs need rebalancing', self.lhs, self.rhs)
            if len(self.lhs) > len(self.rhs):
                popped_elem = heapq.heappop(self.lhs)
                heapq.heappush(self.rhs, -popped_elem)
            else:
                popped_elem = heapq.heappop(self.rhs)
                heapq.heappush(self.lhs, -popped_elem)
        print('Post rebalancing', self.lhs, self.rhs)
        print('EOF ADD METHOD')

    def findMedian(self) -> float:
        tl = len(self.lhs) + len(self.rhs)
        print('FIND MEDIAN', tl)
        if (tl%2)>0:
            # odd
            print('odd')
            if len(self.lhs)>len(self.rhs):
                return -self.lhs[0]
            else:
                return self.rhs[0]
        print('even')
        return (-self.lhs[0]+self.rhs[0])/2