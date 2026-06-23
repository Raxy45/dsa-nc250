class FreqStack:

    def __init__(self):
        self.fmp = defaultdict(int)
        self.c_hmp = [[]]

    def push(self, val: int) -> None:
        count = 1
        if val not in self.fmp:
            self.fmp[val] = 1
            count = 1
        else:
            self.fmp[val] += 1
            count = self.fmp[val]
        
        if count>=len(self.c_hmp):
            self.c_hmp.append([val])
        else:
            self.c_hmp[count].append(val)

    def pop(self) -> int:
        max_count = len(self.c_hmp)
        ans = self.c_hmp[-1].pop()

        if len(self.c_hmp[-1]) == 0:
            self.c_hmp.pop()
        return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()