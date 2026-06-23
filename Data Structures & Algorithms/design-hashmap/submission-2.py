class MyHashMap:

    def __init__(self):
        self.data = [-1 for i in range(10**6+1)]

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data[key]

    def remove(self, key: int) -> None:
        self.data[key] = -1

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashSet = [ListNode(0, 0) for i in range(1000)]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.hashSet)
        current_key_index = self.hashSet[index]
        # print('index ', index)
        while current_key_index.next:
            if current_key_index.next.key == key:
                current_key_index.next.value = value
                return
            current_key_index = current_key_index.next
        # print(current_key_index.key, current_key_index.value, 'og key', key, value)
        current_key_index.next = ListNode(key, value)
        # print(self.hashSet)

    def get(self, key: int) -> int:
        index = key % len(self.hashSet)
        # print('index', index)
        current_key_index = self.hashSet[index].next
        while current_key_index:
            print(current_key_index.key)
            if current_key_index.key == key:
                # print('found key', key)
                return current_key_index.value
            current_key_index = current_key_index.next
            # print(current_key_index.next)
        return -1

    def remove(self, key: int) -> None:
        index = key % len(self.hashSet)
        current_key_index = self.hashSet[index]
        while current_key_index.next:
            if current_key_index.next.key == key:
                current_key_index.next = current_key_index.next.next
                return
            current_key_index = current_key_index.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)