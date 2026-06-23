class MinStack:

    def __init__(self):
        self.data = []
        self.s_min_data = []
        self.prev_min = sys.maxsize       

    def push(self, val: int) -> None:
        print('in push,val: ', val)
        print(self.data)
        print(self.s_min_data)
        if val < self.prev_min:
            self.prev_min = val
        self.s_min_data.append(self.prev_min)
        self.data.append(val)

    def pop(self) -> None:
        print('in pop')
        print(self.data)
        print(self.s_min_data)
        self.data.pop()
        self.s_min_data.pop()

    def top(self) -> int:
        print('in top')
        print(self.data)
        print(self.s_min_data)
        return self.data[-1]

    def getMin(self) -> int:
        print('in getMin')
        print(self.data)
        print(self.s_min_data)
        return self.s_min_data[-1]
