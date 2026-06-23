from collections import defaultdict

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:
    """Doubly linked list for LRU within same frequency"""
    def __init__(self):
        self.left = Node()   # dummy head
        self.right = Node()  # dummy tail
        self.left.next = self.right
        self.right.prev = self.left

    def is_empty(self):
        return self.left.next == self.right

    def add(self, node):
        # insert at tail (most recently used)
        last = self.right.prev
        last.next = node
        node.prev = last
        node.next = self.right
        self.right.prev = node

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def pop_left(self):
        # remove least recently used
        if self.is_empty():
            return None
        node = self.left.next
        self.remove(node)
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        self.key_map = {}              # key -> node
        self.freq_map = defaultdict(DLL)  # freq -> DLL
        self.min_freq = 0

    def _increase_freq(self, node):
        freq = node.freq
        self.freq_map[freq].remove(node)

        # update min_freq if needed
        if freq == self.min_freq and self.freq_map[freq].is_empty():
            del self.freq_map[freq]
            self.min_freq += 1

        node.freq += 1
        self.freq_map[node.freq].add(node)

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1

        node = self.key_map[key]
        self._increase_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        # Update existing key
        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self._increase_freq(node)
            return

        # Evict if full
        if self.size == self.capacity:
            lru = self.freq_map[self.min_freq].pop_left()
            del self.key_map[lru.key]
            self.size -= 1

        # Insert new node
        node = Node(key, value)
        self.key_map[key] = node
        self.freq_map[1].add(node)
        self.min_freq = 1
        self.size += 1