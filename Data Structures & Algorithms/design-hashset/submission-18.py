class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.n = 100
        self.vals = [Node(0) for _ in range(10001)]

    def get_key(self, val):
        return val % self.n

    def add(self, key: int) -> None:
        curr = self.vals[self.get_key(key)]
        while curr.next:
            if curr.val == key: return
            curr = curr.next
        curr.next = Node(key)

    def remove(self, key: int) -> None:
        curr = self.vals[self.get_key(key)]
        while curr and curr.next :
            if curr.next.val == key: 
                print('removed',key)
                curr.next = curr.next.next
                continue
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.vals[self.get_key(key)]
        while curr:
            if curr.val == key: return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)