class StockSpanner:

    def __init__(self):
        self.mon_stk = []

    def next(self, price: int) -> int:
        ans = 1
        if len(self.mon_stk) == 0:
            self.mon_stk.append((1, price))
            return ans
        
        print(self.mon_stk)
        if price < self.mon_stk[-1][1]:
            print('price < last stack element')
            self.mon_stk.append((ans, price))
            return ans
        
        while len(self.mon_stk) > 0 and price>=self.mon_stk[-1][1]:
            ans += self.mon_stk[-1][0]
            self.mon_stk.pop()

        self.mon_stk.append((ans, price))
        return ans
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)