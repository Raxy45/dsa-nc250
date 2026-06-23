class ListNode:
    def __init__(self, val=None, next_ptr=None):
        self.val = val
        self.next = next_ptr
    
class MyCircularQueue:

    def __init__(self, k: int):
        self.q_len = k
        self.head = self.tail = ListNode()  
        self.curr_len = 0  

    def enQueue(self, value: int) -> bool:
        if self.curr_len>=self.q_len:
            return False
        curr_node = ListNode(value)
        self.tail.next = curr_node
        if self.curr_len == 0:
            self.start = self.tail
        self.tail = self.tail.next
        self.curr_len += 1
        return True

    def deQueue(self) -> bool:
        if not self.start:
            return False
        popped_elem = self.start.val
        self.start = self.start.next
        self.curr_len -= 1
        return True

    def Front(self) -> int:
        return self.start.val if self.start else -1

    def Rear(self) -> int:
        return self.tail.val if self.tail else -1

    def isEmpty(self) -> bool:
        return self.curr_len == 0

    def isFull(self) -> bool:
        return self.curr_len == self.q_len


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()