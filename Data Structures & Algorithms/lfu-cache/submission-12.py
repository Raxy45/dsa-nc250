from collections import defaultdict


class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRU:
    def __init__(self):
        # start -> LRU ... MRU -> end
        self.start = Node()
        self.end = Node()

        self.start.next = self.end
        self.end.prev = self.start

    def isEmpty(self):
        return self.start.next == self.end

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def add(self, node):
        # Add as MRU
        last = self.end.prev

        last.next = node
        node.prev = last

        node.next = self.end
        self.end.prev = node

    def remove_lru_node(self):
        if self.isEmpty():
            return None

        lru_node = self.start.next
        self.remove(lru_node)

        return lru_node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_capacity = 0

        # key -> Node
        self.node_map = {}

        # Node -> frequency
        self.freq_map = {}

        # frequency -> LRU list
        self.lfu = defaultdict(LRU)

        # minimum frequency currently present
        self.min_freq = 0

    def useCounter(self, node):
        curr_freq = self.freq_map[node]
        updated_freq = curr_freq + 1

        # Remove from old frequency bucket
        old_lru = self.lfu[curr_freq]
        old_lru.remove(node)

        if old_lru.isEmpty():
            del self.lfu[curr_freq]

            # IMPORTANT:
            # Only update min_freq if the bucket that became
            # empty was actually the minimum-frequency bucket.
            if curr_freq == self.min_freq:
                self.min_freq = updated_freq

        # Add to new frequency bucket
        self.lfu[updated_freq].add(node)
        self.freq_map[node] = updated_freq

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1

        node = self.node_map[key]

        self.useCounter(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        # Capacity 0
        if self.capacity == 0:
            return

        # Existing key
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value

            self.useCounter(node)
            return

        # Cache full -> evict LFU + LRU among that frequency
        if self.curr_capacity == self.capacity:

            lru = self.lfu[self.min_freq]

            popped_node = lru.remove_lru_node()

            # Remove completely from cache
            del self.node_map[popped_node.key]
            del self.freq_map[popped_node]

            self.curr_capacity -= 1

            if lru.isEmpty():
                del self.lfu[self.min_freq]

        # Add new node
        new_node = Node(key, value)

        self.node_map[key] = new_node

        # New node always starts at frequency 1
        self.freq_map[new_node] = 1
        self.lfu[1].add(new_node)

        self.min_freq = 1

        self.curr_capacity += 1