class MyHashSet:

    class ListNode:
        def __init__(self, data):
            self.next=None
            self.data = data
        
    def __init__(self):
        self.HashSet = [self.ListNode(0) for i in range(10000)]

    def get_index(self, data):
        idx = data%10000
        return idx

    def add(self, key: int) -> None:
        current_idx = self.get_index(key)
        print(current_idx, 'c_idx')
        current_node = self.HashSet[current_idx]
        while current_node.next:
            if current_node.next.data == key:
                return
            current_node = current_node.next
        
        new_node = self.ListNode(key)
        current_node.next = new_node 

    def remove(self, key: int) -> None:
        current_idx = self.get_index(key)
        current_node = self.HashSet[current_idx]
        while current_node.next:
            if current_node.next.data ==  key:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def contains(self, key: int) -> bool:
        current_idx = self.get_index(key)
        print('in contains')
        print(key, current_idx)
        current_node = self.HashSet[current_idx]
        while current_node.next:
            print('data', current_node.data)
            if current_node.next.data == key:
                return True
            current_node = current_node.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)