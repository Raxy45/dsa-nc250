class ListNode:
    def __init__(self, value, key, next, prev):
        self.val, self.key, self.next, self.prev = value, key, next, prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.allowed_capacity = capacity
        self.hmp = {}
        self.ll = None
        self.start = self.end = None

    def get(self, key: int) -> int:
        if key not in self.hmp:
            return -1
        required_node = self.hmp[key]
        if self.end == required_node:
            return self.end.val
        prev, after = required_node.prev, required_node.next
        if prev:
            prev.next = after
        if after:
            after.prev = prev
        self.end.next, required_node.prev = required_node, self.end
        required_node.next = None
        self.end = self.end.next
        return required_node.val

    def put(self, key: int, value: int) -> None:
        print(self.capacity)
        if key in self.hmp:
            required_node = self.hmp[key]
            required_node.val = value
            self.get(key) # this will also bring the element to the end of the list
            return
        else:
            required_node = ListNode(value, key, None, None)
            self.hmp[key] = required_node
        
        if self.capacity == 0:
            # pop out first elem
            print('poping out elem from start for ', key, value)
            self.hmp.pop(self.start.key)
            self.start = self.start.next
            self.start.prev = None
            self.capacity += 1
        
        if not self.end:
            # first element to be added
            self.start = self.end = required_node
            self.capacity -= 1
            return
        self.end.next = required_node
        required_node.next = None
        required_node.prev = self.end
        self.end = self.end.next
        self.capacity -= 1