class Node:
    def __init__(self, key=0, val=0,next=None,prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.k=capacity
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left
        self.key_map = {}

    def add(self, node):
        prev_lru = self.right.prev

        prev_lru.next = node
        node.prev = prev_lru
        node.next = self.right
        self.right.prev = node

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1 
        consumed_node = self.key_map[key]
        self.remove(consumed_node)
        self.add(consumed_node)
        return self.key_map[key].val

    def isEmpty(self):
        return self.left.next == self.right

    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            node = self.key_map[key]
            node.val = value
            self.remove(node)
            self.add(node)
            return

        if self.k==0:
            if self.isEmpty(): return
            lru_node = self.left.next
            del self.key_map[lru_node.key]
            self.remove(lru_node.next)
            del lru_node
            self.k += 1
        
        new_node = Node(key, value)
        self.add(new_node)
        self.key_map[key] = new_node
        self.k -= 1

        
