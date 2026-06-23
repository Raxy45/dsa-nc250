class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node()
        self.right = Node(prev=self.left)
        self.left.next = self.right
        self.key_map = {}

    def get(self, key: int) -> int:
        if key not in self.key_map: return -1
        node = self.key_map[key]
        self.remove(node)
        self.put(node.key, node.val)
        return node.val

    def put(self, key: int, value: int) -> None:
        print('Inserting',key)
        if key in self.key_map:
            print('key', key,'already exists in key_map')
            old_node = self.key_map[key]
            self.remove(old_node)
        
        if self.capacity == 0:
            print('capacity exhausted')
            self.remove(self.left.next)

        new_node = Node(key, value)
        self.key_map[key] = new_node
        prev_latest_node = self.right.prev
        prev_latest_node.next = new_node
        self.right.prev = new_node
        new_node.prev, new_node.next = prev_latest_node, self.right
        self.capacity -= 1
        print('insertion completed')

    def remove(self, node):
        prev, after = node.prev, node.next
        prev.next, after.prev = after, prev
        del self.key_map[node.key]
        del node
        self.capacity += 1