class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = []
        for stone in stones:
            heapq.heappush(hp, -stone)
        while len(hp)>1:
            stone_a = abs(heapq.heappop(hp))
            stone_b = abs(heapq.heappop(hp))
            if stone_a == stone_b: continue
            heapq.heappush(hp, -abs(stone_a - stone_b))
        return abs(hp[0]) if len(hp)>0 else 0