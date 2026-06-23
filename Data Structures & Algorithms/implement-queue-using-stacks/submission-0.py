class MyQueue:

    def __init__(self):
        self.stack1, self.stack2 = [], []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        cur_len = len(self.stack1)
        for _ in range(cur_len-1):
            popped_elem = self.stack1.pop()
            self.stack2.append(popped_elem)
        ans = self.stack1.pop()

        self.stack1 = self.stack2[::-1]
        self.stack2 = []
        return ans

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()