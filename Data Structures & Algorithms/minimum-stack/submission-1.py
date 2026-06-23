class MinStack:

    def __init__(self):
        self.data = []
        self.s_min_data = []
        self.prev_min = sys.maxsize       

    def push(self, val: int) -> None:
        print('in push,val: ', val)
        if val < self.prev_min:
            self.prev_min = val
        self.s_min_data.append(self.prev_min)
        self.data.append(val)
        print(self.data)
        print(self.s_min_data)

    def pop(self) -> None:
        print('in pop')
        self.data.pop()
        self.s_min_data.pop()
        print(self.data)
        print(self.s_min_data)

    def top(self) -> int:
        print('in top')
        return self.data[-1]

    def getMin(self) -> int:
        print('in getMin')
        print(self.data)
        print(self.s_min_data)
        return self.s_min_data[-1]
