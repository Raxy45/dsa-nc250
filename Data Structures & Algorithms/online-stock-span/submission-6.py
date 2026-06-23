class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        count = 1
        while self.stk and price > self.stk[-1][0]:
            count += self.stk.pop()[1]

        self.stk.append((price, count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)