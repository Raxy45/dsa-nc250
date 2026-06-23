class Node:
    def __init__(self, key=0,value=0, freq=1, next=None,prev=None):
        self.key, self.value = key, value
        self.next, self.prev = next, prev
        self.freq = freq
class LRUCache:
    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next, self.right.prev = self.right, self.left
        self.key_map = {}

    def isEmpty(self):
        return self.left.next == self.right

    def isFull(self):
        pass
    
    def add(self, node):
        print('     LRU: Adding key:val', node.key, node.value)
        current_last = self.right.prev
        current_last.next, self.right.prev = node, node
        node.prev, node.next = current_last, self.right
        self.key_map[node.key] = node

    def remove_least(self):
        self.remove(self.left.next)

    def get(self, key):
        if key not in self.key_map: return None
        return self.key_map[key]

    def remove(self, node):
        print('     LRU: removing key', node.key)
        if node.key not in self.key_map:
            return
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        del self.key_map[node.key]
        del node

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}
        self.lfu = defaultdict(LRUCache)
        self.least_used = -1        

    def get(self, key: int) -> int:
        print('LFU: performing get for',key)
        if key not in self.key_map:
            print('LFU: key not in key_map')
            return -1
        
        node = self.key_map[key]
        freq = node.freq
        node.freq += 1
        updated_freq = freq + 1
        
        print('Updating freq of key', key, 'from', freq, 'to', updated_freq)
        old_lru = self.lfu[freq]
        old_lru.remove(node)
        if old_lru.isEmpty():
            del self.lfu[freq]
            if self.least_used == freq:
                self.least_used = updated_freq

        print('Adding key', key, 'to new freq lru', updated_freq)
        updated_freq_lru = self.lfu[updated_freq]
        updated_freq_lru.add(node)
        print('Updated lfu', self.lfu)
        return node.value

    def put(self, key: int, value: int) -> None:
        print('LFU: Performing put for', key, value)
        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self.get(node)
            return
        
        if self.capacity == 0:
            least_used_lru = self.lfu[self.least_used]
            to_be_removed_node = least_used_lru.left.next
            del self.key_map[to_be_removed_node.key]
            print('LFU: capacity exhausted, popping out elem from least used lru', self.least_used)
            least_used_lru.remove_least()
            if least_used_lru.isEmpty():
                del self.lfu[self.least_used]
                self.least_used = -1
            self.capacity += 1
        
        self.key_map[key] = Node(key, value)
        current_lru = self.lfu[1]
        current_lru.add(self.key_map[key])
        if self.least_used == -1:
            self.least_used = 1
        self.capacity -= 1
        print('After adding', key)
        print('least freq', self.least_used)
        print('LFU', self.lfu)
            


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)