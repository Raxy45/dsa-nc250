class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.allowed_capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0, self.left)
        self.left.next = self.right
        self.key_map = {}

    def get(self, key: int) -> int:
        if key not in self.key_map: return -1
        required_node = self.key_map[key]
        self.remove_node(required_node)
        self.add_node(required_node)
        return required_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            node_to_be_updated = self.key_map[key]
            self.remove_node(node_to_be_updated)

        if self.allowed_capacity == 0:
            least_used_node = self.left.next
            self.remove_node(least_used_node)
            del self.key_map[least_used_node.key]

        new_node = Node(key, value)
        self.add_node(new_node)
        self.key_map[key] = new_node

    def remove_node(self, node):
        
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        self.allowed_capacity += 1
        return

    def add_node(self, node):

        current_last = self.right.prev
        current_last.next, node.prev = node, current_last
        node.next, self.right.prev = self.right, node
        self.allowed_capacity -= 1

