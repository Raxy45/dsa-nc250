class MyStack:
    def __init__(self):
        self.q1 = deque()

    def push(self, x):
        self.q1.append(x)
        popped_elems = len(self.q1)
        c = 0
        while c<popped_elems-1:
            self.q1.append(self.q1.popleft())
            c+=1

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]
    
    def __init__(self):
        self.q1 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        cur_len = len(self.q1)
        pop_elem = -1
        for i in range(cur_len-1):
            pop_elem = self.q1.popleft()
            self.q1.append(pop_elem)

        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return len(self.q1) == 0
class MyStackTwoQueue:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        popped_val = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1

        return popped_val
        
    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return len(self.q1) == 0