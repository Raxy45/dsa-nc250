class ListNode:
    def __init__(self, val=None, next_ptr=None):
        self.val = val
        self.next = next_ptr
    
class MyCircularQueue:

    def __init__(self, k: int):
        self.q_len = k
        self.start = self.tail = ListNode()  
        self.curr_len = 0  

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        curr_node = ListNode(value)
        self.tail.next = curr_node
        if self.curr_len == 0:
            print('assigning start to ', value)
            self.start = curr_node
        self.tail = self.tail.next
        self.curr_len += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        popped_elem = self.start.val
        self.start = self.start.next
        self.curr_len -= 1
        return True

    def Front(self) -> int:
        # print('self.start', self.start)
        return self.start.val if self.start and self.curr_len>0 else -1
# ["MyCircularQueue","enQueue","deQueue","deQueue","Front","Rear","isEmpty"]
# [[1],[5],[],[],[],[],[]]
    def Rear(self) -> int:
        return self.tail.val if self.tail and self.curr_len>0 else -1

    def isEmpty(self) -> bool:
        return self.curr_len == 0

    def isFull(self) -> bool:
        return self.curr_len == self.q_len