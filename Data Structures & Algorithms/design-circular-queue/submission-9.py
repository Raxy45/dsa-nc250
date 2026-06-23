class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.current_capacity = k
        self.left = Node()
        self.right = Node(0, prev=self.left)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        second_last = self.right.prev
        new_node = Node(value, prev=second_last, next=self.right)
        second_last.next, self.right.prev = new_node, new_node
        self.current_capacity -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        new_first = self.left.next.next
        to_be_deleted = self.left.next
        self.left.next = new_first
        new_first.prev = self.left
        del to_be_deleted
        self.current_capacity += 1
        return True
        
    def Front(self) -> int:
        if not self.isEmpty():
            return self.left.next.val
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.right.prev.val
        return -1

    def isEmpty(self) -> bool:
        return self.left.next==self.right

    def isFull(self) -> bool:
        return self.current_capacity == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()