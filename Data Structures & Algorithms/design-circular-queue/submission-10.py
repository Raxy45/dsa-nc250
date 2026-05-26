class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.left = ListNode()
        self.right = ListNode(99)
        self.left.next = self.right
        self.right.prev = self.left
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        new_node = ListNode(value)
        prev_rear = self.right.prev
        new_node.next, new_node.prev = self.right, prev_rear
        prev_rear.next, self.right.prev = new_node, new_node
        self.k -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        popped = self.left.next
        self.left.next, popped.next.prev = popped.next, self.left
        del popped
        self.k += 1
        return True

    def Front(self) -> int:
        return self.left.next.val if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.right.prev.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        print('isEmpty Check')
        print(self.left.next.val, self.right.val)
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.k == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()