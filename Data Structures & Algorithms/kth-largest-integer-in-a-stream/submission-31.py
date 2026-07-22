class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hp = []
        self.k = k
        for n in nums:
            heapq.heappush(self.hp, n)
            if len(self.hp) > k:
                heapq.heappop(self.hp)
        # print(self.hp)

    def add(self, val: int) -> int:
        heapq.heappush(self.hp, val)
        if len(self.hp) > self.k:
            heapq.heappop(self.hp)
        return self.hp[0]
       