class StockSpanner:

    def __init__(self):
        self.mon_stk = []

    def next(self, price: int) -> int:
        if len(self.mon_stk)==0:
            self.mon_stk.append((1, price))
            return 1
        ans = 1

        while len(self.mon_stk)>0 and self.mon_stk[-1][1]<=price:
            ans+=self.mon_stk[-1][0]
            self.mon_stk.pop()
        
        self.mon_stk.append((ans, price))
        return ans
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)