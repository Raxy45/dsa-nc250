class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ll_hmp = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove_node(self, node):
        prev, after = node.prev, node.next
        prev.next, after.prev = after, prev
        del self.ll_hmp[node.key]

    def insert_node(self, node):
        prev, after = self.right.prev, self.right
        prev.next = after.prev = node
        node.prev = prev
        node.next = after
        self.ll_hmp[node.key] = node
        
    def get(self, key: int) -> int:
        if key not in self.ll_hmp: return -1

        req_node = self.ll_hmp[key]
        self.remove_node(req_node)
        self.insert_node(req_node)
        return req_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.ll_hmp:
            self.remove_node(self.ll_hmp[key])
        
        new_node = Node(key, value)
        self.insert_node(new_node)
        if len(self.ll_hmp) > self.capacity:
            self.remove_node(self.left.next)
