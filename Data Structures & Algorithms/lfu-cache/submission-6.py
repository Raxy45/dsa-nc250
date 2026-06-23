class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None, freq=0):
        self.key, self.val = key, val
        self.next, self.prev = next, prev
        self.freq = freq

class LRU:
    def __init__(self):
        self.key_map = {}
        self.left, self.right = ListNode(), ListNode()
        self.left.next, self.right.prev = self.right, self.left

    def isEmpty(self):
        return self.left.next == self.right
    
    def remove(self, node):
        prev_node, next_node = node.prev, node.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        
        del node

    def insert(self, node):
        prev_ru = self.right.prev
        prev_ru.next, self.right.prev = node, node
        node.prev, node.next = prev_ru, self.right
    
    def remove_lru(self):
        self.remove(self.left.next)

class LFUCache:

    def __init__(self, capacity: int):
        self.k = capacity
        self.lru_map = defaultdict(LRU)
        self.global_mp = defaultdict(ListNode)
        self.lowest_freq = float('inf')
        

    def get(self, key: int) -> int:
        if key not in self.global_mp:
            return -1
        
        node = self.global_mp[key]
        self.useCounter(node)
        return node.val
    
    def useCounter(self, node):
        current_freq = node.freq
        current_lru = self.lru_map[current_freq]
        current_lru.remove(node)
        if current_lru.isEmpty():
            del self.lru_map[current_freq]
            if current_freq == self.lowest_freq:
                self.lowest_freq += 1
        
        new_freq = node.freq = current_freq + 1
        new_lru = self.lru_map[new_freq]
        new_lru.insert(node)

    def put(self, key: int, value: int) -> None:
        if key in self.global_mp:
            node = self.global_mp[key]
            node.val = value
            useCounter(node)
            return
        
        # key does not exist
        if self.k == 0:
            lfu_lru = self.lru_map[self.lowest_freq]
            popped_node = lfu_lru.left.next
            lfu_lru.remove_lru()
            del self.global_mp[popped_node.key]
            if lfu_lru.isEmpty():
                del self.global_mp[self.lowest_freq]
                self.lowest_freq += 1
        new_node = ListNode(key, value, None, None, 1)
        self.global_mp[key] = new_node
        self.lru_map[1].insert(new_node)
        self.lowest_freq = min(self.lowest_freq, 1)
        # self.global_mp[1].insert(node_node)
        self.k -= 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)