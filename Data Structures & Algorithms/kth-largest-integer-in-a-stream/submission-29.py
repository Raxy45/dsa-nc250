class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hp = []
        for n in nums:
            heapq.heappush(self.hp, n)
            if len(self.hp) > k:
                heapq.heappop(self.hp)
        # print(self.hp)

    def add(self, val: int) -> int:
        if val < self.hp[0]:
            return self.hp[0]
        heapq.heappush(self.hp, val)
        heapq.heappop(self.hp)
        return self.hp[0]
       