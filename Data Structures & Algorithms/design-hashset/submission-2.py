class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hashSet = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        index = key % len(self.hashSet)
        current_key_index = self.hashSet[index]
        while current_key_index.next:
            if current_key_index.next.key == key:
                return
            current_key_index = current_key_index.next
        current_key_index.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % len(self.hashSet)
        current_key_index = self.hashSet[index]
        while current_key_index.next:
            if current_key_index.next.key == key:
                current_key_index.next = current_key_index.next.next
                return
            current_key_index = current_key_index.next

    def contains(self, key: int) -> bool:
        index = key % len(self.hashSet)
        current_key_index = self.hashSet[index]
        while current_key_index.next:
            if current_key_index.next.key == key:
                return True
            current_key_index = current_key_index.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)