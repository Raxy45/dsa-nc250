class FreqStack:

    def __init__(self):
        self.count_dict = {}
        self.freq_stk = [[]]

    def push(self, val: int) -> None:
        print('val ', val)
        print(self.count_dict)
        print(self.freq_stk)
        self.count_dict[val] = self.count_dict.get(val, 0) + 1
        current_freq = self.count_dict[val]
        if current_freq >= len(self.freq_stk):
            print('current_freq in first', current_freq)
            # print(self.count_dict)
            # print(self.freq_stk)
            self.freq_stk.append([val])
        else:
            print('current_freq ', current_freq)
            self.freq_stk[current_freq].append(val)
        print(self.freq_stk)
        print('after')

    def pop(self) -> int:
        # print('in pop')
        # print(self.freq_stk)
        while len(self.freq_stk) > 0 and len(self.freq_stk[-1]) == 0:
            self.freq_stk.pop() # -> empty ones popped out
        print(self.freq_stk[-1])
        print('befor eerr')
        last_elem = self.freq_stk[-1].pop()
        self.count_dict[last_elem] -= 1
        return last_elem


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()