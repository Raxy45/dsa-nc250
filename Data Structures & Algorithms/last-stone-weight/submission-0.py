class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        while len(stones) > 1:
            stone_a, stone_b = stones.pop(), stones.pop()
            if stone_a == stone_b: continue
            else:
                heapq.heappush(stones, 
                max(stone_a, stone_b) - min(stone_a, stone_b))
        if not stones: return 0
        return stones[0]