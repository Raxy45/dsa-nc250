class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MyCircularQueue:

    def __init__(self, k: int):
        self.allowed_capacity = k
        self.capacity = k
        self.left = Node(0)
        self.right = Node(0, self.left)
        self.left.right = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        new_node = Node(value, self.right.left, self.right)
        self.right.left.right = new_node
        self.right.left = new_node
        self.capacity -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        popped = self.left.right

        popped.left = self.left
        self.left.right = popped.right
        self.capacity += 1
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.left.right.val
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.right.left.val
        return -1

    def isEmpty(self) -> bool:
        return self.allowed_capacity == self.capacity

    def isFull(self) -> bool:
        return self.capacity == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()