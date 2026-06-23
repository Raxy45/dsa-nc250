class MyQueue:
    def __init__(self):
        self.stack1, self.stack2 = [], []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self):
        if len(self.stack2) > 0:
            poped_elem =  self.stack2.pop()
            return poped_elem
        
        while len(self.stack1)-1 > 0:
            self.stack2.append(self.stack1.pop())

        return self.stack1.pop()


    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return max(len(self.stack1), len(self.stack2)) == 0


class MyQueueEasy:

    def __init__(self):
        self.stack1, self.stack2 = [], []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self):
        if len(self.stack2) > 0:
            poped_elem =  self.stack2.pop()
            return poped_elem
        
        while len(self.stack1)-1 > 0:
            self.stack2.append(self.stack1.pop())

        return self.stack1.pop()


    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return len(self.stack1) == 0










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