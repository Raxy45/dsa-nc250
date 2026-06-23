class ListNode:
    def __init__(self, key, value):
        self.val, self.key = value, key
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.hmp = {}
        self.left, self.right = ListNode(0, 0), ListNode(0,0)
        self.left.next , self.right.prev = self.right, self.left
        self.allowed_capacity = capacity

    def remove_node(self, node):
        before, after = node.prev, node.next
        before.next, after.prev = after, before
        
    def append_node(self, node):
        prev, after = self.right.prev, self.right
        prev.next, after.prev = node, node
        node.prev, node.next = prev, after
     
    def get(self, key: int) -> int:
        if key in self.hmp:
            current_node = self.hmp[key]
            self.remove_node(current_node)
            self.append_node(current_node)
            return current_node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmp:
            self.remove_node(self.hmp[key])
        
        self.hmp[key] = ListNode(key, value)
        self.append_node(self.hmp[key])
        if len(self.hmp) > self.allowed_capacity:
            # remove left most elem
            left_most_elem = self.left.next
            self.remove_node(left_most_elem)
            self.hmp.pop(left_most_elem.key)
