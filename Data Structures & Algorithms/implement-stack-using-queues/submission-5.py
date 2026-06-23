class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        if not self.q:
            self.q.append(x)
            return
        
        self.q.append(x)
        curr_len = len(self.q)
        while curr_len>1:
            popped = self.q.popleft()
            self.q.append(popped)
            curr_len -= 1
        
    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()