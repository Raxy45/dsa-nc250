class MyHashSet:

    def __init__(self):
        self.data = []

    def add(self, key: int) -> None:
        # print(f'adding {key}')
        # print(self.data)
        self.data.append(key)

    def remove(self, key: int) -> None:
        # print(f'remove {key}')
        # print(self.data)
        new_data = []
        for i in self.data:
            if i != key:
                new_data.append(i)
        self.data = new_data

    def contains(self, key: int) -> bool:
        # print(f'{key} in {self.data}')
        for i in self.data:
            if i == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)