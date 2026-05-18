class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class MyHashSet:
    def __init__(self):
        pass
    
    def add(key):
        r_key = key % 10000
        curr = self.HS[r_key]
        while curr.next:
            curr = curr.next
            
        new_node = Node(key)
        curr.next = new_node
        return
    
    def contains(key):
        r_key = key % 10000
        curr = self.HS[r_key]
        curr = curr.next
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    def remove(key):
        r_key = key % 10000
        curr = self.HS[r_key]
        while curr.next:
            if curr.next.data == key:
                curr.next = curr.next.next
            else:
                curr = curr.next
        




class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class MyHashSet:

    def __init__(self):
        self.key_map = [Node(0) for _ in range(10001)]

    def get_key(self, num):
        return num%10000

    def add(self, key: int) -> None:
        index = self.get_key(key)
        slot = self.key_map[index]

        while slot and slot.next!=None:
            if slot.data == key:
                return
            slot = slot.next
        
        # print(slot, key)
        if slot.data == key:
            return
        new_node = Node(key)
        slot.next = new_node
        return

    def remove(self, key: int) -> None:
        index = self.get_key(key)
        slot = self.key_map[index]

        while slot and slot.next and slot.next.data!=key:
            print(slot.next, slow.next.data, key, 'in?')
            slot = slot.next
        
        if not slot.next:
            return

        print(slot, slot.data, key)
        slot.next = slot.next.next
        print(slot.next)
        return

    def contains(self, key: int) -> bool:
        print('in contains')
        index = self.get_key(key)
        slot = self.key_map[index].next

        while slot and slot.data!=key:
            slot = slot.next
        
        if not slot:
            print('False for', key)
            return False
        # print(slot, slot.data, key)
        print('True for', key)
        return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)