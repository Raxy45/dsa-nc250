class ListNode:
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key, self.val = key, value
        self.prev, self.next = prev, next

class LRUCache:

    def __init__(self, capacity: int):
        self.k = capacity
        self.left = ListNode()
        self.right = ListNode()
        self.left.next, self.right.prev = self.right, self.left
        self.key_map = {}

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        
        node = self.key_map[key]
        prev_node, post_node = node.prev, node.next
        prev_node.next, post_node.prev = post_node, prev_node
        self.put(key, node.val)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            node = self.key_map[key]
            nodes_left, nodes_right = node.prev, node.next
            nodes_left.next, nodes_right.prev = nodes_right, nodes_left
        else:
            if self.k == 0:
            # remove lru
                lru = self.left.next
                self.left.next, lru.next.prev = lru.next, self.left
                print('deleting', lru.key, lru.val, 'for', key, value)
                del self.key_map[lru.key]
                del lru
                self.k += 1

            node = ListNode(key, value)
            self.key_map[key] = node
            self.k -= 1
        
        print('for key', key, value)
        print(self.key_map)
        node.val = value
        prev_node = self.right.prev
        prev_node.next = node
        node.prev = prev_node
        self.right.prev = node
        node.next = self.right
        

