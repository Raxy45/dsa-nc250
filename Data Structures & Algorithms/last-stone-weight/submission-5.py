class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = []
        for stone in stones:
            hp.append(-stone)
        
        heapq.heapify(hp)
        while len(hp) > 1:
            stone_a, stone_b = abs(heapq.heappop(hp)), abs(heapq.heappop(hp))
            if stone_a == stone_b:
                continue
            leftover = max(stone_a, stone_b) - min(stone_a, stone_b)
            heapq.heappush(hp, -leftover)
        
        return -hp[0] if hp else 0
            

        