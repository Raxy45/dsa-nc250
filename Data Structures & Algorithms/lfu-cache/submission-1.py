

class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.value = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self):
        self.left = Node(0, 0)
        self.right = Node(0, 0, self.left)
        self.left.next = self.right

    def remove_node(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        return

    def add_node(self, node):
        current_last = self.right.prev
        current_last.next, node.prev = node, current_last
        node.next, self.right.prev = self.right, node
    
    def pop_left(self):
        next_node = self.left.next.next
        print('in pop left, removing node with key, value', self.left.next.key, self.left.next.value)
        self.left.next, next_node.prev = next_node, self.left
        return
    
    def isEmpty(self):
        return self.left.next == self.right


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq_map = defaultdict(int)
        self.key_map = defaultdict(Node)
        self.freq_ll = defaultdict(LRUCache)
        self.lowest_freq = float('inf')

    def counter(self, node):
        # updating frequency in frequency map
        old_freq = self.freq_map[node.key]
        updated_freq = old_freq + 1
        self.freq_map[node.key] = updated_freq
        print('moving node with k,v',node.key, node.value, 'from old lru to new lru', old_freq, updated_freq)
        # moving node from old freq lru to updated freq lru
        old_freq_lru = self.freq_ll[old_freq]
        old_freq_lru.remove_node(node) # -> removed from old lru
        
        # adding node to new freq map
        updated_freq_lru = self.freq_ll[updated_freq]
        updated_freq_lru.add_node(node)

        # updating least freq if needed:
        if self.lowest_freq == old_freq:
            print('current lowest frequency is set to old frequency')
            if old_freq_lru.isEmpty():
                print('updating lowest frequency to new since old lru is empty', updated_freq)
                self.lowest_freq = updated_freq
        
    def get(self, key: int) -> int:
        if key not in self.key_map: return -1

        required_node = self.key_map[key]
        # update the frequence of node
            # move from old freq lru to new freq lru
            # if old freq was least and old freq lru is empty, update least freq lru to updated
        self.counter(required_node)
        return required_node.value

    def put(self, key: int, value: int) -> None:
        print('doing put operation for', key, value)
        # if key already exists, update the value of key and set its freq to old freq + 1
        if key in self.key_map:
            required_node = self.key_map[key]
            required_node.value = value # value updated in the node
            self.counter(required_node) # this will update the frequency of the node
            return
        
        if self.capacity == 0:
            # no space left, get the LRU with least frequency -> then pop the one which is least used(present at first place)
            lru_with_least_frequency = self.freq_ll[self.lowest_freq]
            print('capacity is 0, popping element with leadt frequency', lru_with_least_frequency)
            node_to_be_popped = lru_with_least_frequency.left.next
            lru_with_least_frequency.pop_left()
            if lru_with_least_frequency.isEmpty():
                self.lowest_freq += 1
            del self.freq_map[node_to_be_popped.key]
            del self.key_map[node_to_be_popped.key]
            self.capacity += 1
        
        # adding element with frequency set as 1(new key)
        frequency = 1
        new_node = Node(key, value)
        self.key_map[key] = new_node
        self.freq_map[key] = frequency
        self.freq_ll[frequency].add_node(new_node)
        self.lowest_freq = min(self.lowest_freq, frequency)
        self.capacity -= 1
        return


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)