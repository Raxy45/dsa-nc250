class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hp = []
        self.k = k
        for n in nums:
            heapq.heappush(self.hp, n)
            if len(self.hp) > k:
                heapq.heappop(self.hp)

    def add(self, val: int) -> int:
        if not self.hp:
            self.hp.append(val)
            return val

        if val < self.hp[0]:
            # no point in adding it to hp
            return self.hp[0]
        
        heapq.heappush(self.hp, val)
        if len(self.hp) > self.k:
            heapq.heappop(self.hp)
        return self.hp[0]
        
