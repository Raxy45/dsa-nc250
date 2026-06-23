class ListNode:
    def __init__(self, key, value):
        self.val, self.key = value, key
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity):
        self.ll_hmp = {}
        self.left, self.right = ListNode(0,0), ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity
    
    def remove_node(self, node):
        prev, after = node.prev, node.after
        prev.next, after.prev = after, prev

    def append_node(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        
    def get(self, key):
        if key not in self.ll_hmp:
            return -1
        
        required_node = self.ll_hmp[key]
        self.remove_node(required_node) # This will remove the node
        self.append_node(required_node) # This will move the node to end to reflect
        return required_node.val        # its used status

    def put(self, key, value):
        if key in self.ll_hmp:
            old_node = self.ll_hmp[key]
            self.remove_node(old_node)
        
        new_node = ListNode(key, value)
        self.append_node(new_node)

        if self.capacity < 0:
            least_used_node = self.left.next
            self.remove_node(least_used_node)
            del self.ll_hmp[least_used_node.key]
            self.capacity += 1
        
    def __init__(self, capacity: int):
        self.hmp = {}
        self.left, self.right = ListNode(0, 0), ListNode(0,0)
        self.left.next , self.right.prev = self.right, self.left
        self.allowed_capacity = capacity

    def remove_node(self, node):
        before, after = node.prev, node.next
        before.next, after.prev = after, before
        
    def append_node(self, node):
        prev, after = self.right.prev, self.right
        prev.next, after.prev = node, node
        node.prev, node.next = prev, after
     
    def get(self, key: int) -> int:
        if key in self.hmp:
            current_node = self.hmp[key]
            self.remove_node(current_node)
            self.append_node(current_node)
            return current_node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmp:
            self.remove_node(self.hmp[key])
        
        self.hmp[key] = ListNode(key, value)
        self.append_node(self.hmp[key])
        if len(self.hmp) > self.allowed_capacity:
            # remove left most elem
            left_most_elem = self.left.next
            self.remove_node(left_most_elem)
            self.hmp.pop(left_most_elem.key)
