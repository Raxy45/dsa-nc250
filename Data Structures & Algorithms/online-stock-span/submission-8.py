class StockSpanner:

    def __init__(self):
        self.stk = []


    def next(self, price: int) -> int:
        curr = 1
        while self.stk and price > self.stk[-1][0]:
            curr += self.stk.pop()[1]
        self.stk.append((price, curr))
        return curr


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)