class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone_a = abs(heapq.heappop(stones))
            print('i', stones)
            stone_b = abs(heapq.heappop(stones))
            print('post', stones)
            if stone_a == stone_b: continue
            else:
                heapq.heappush(stones, 
                -(max(stone_a, stone_b) - min(stone_a, stone_b)))
        print(stones)
        if not stones: return 0
        return abs(stones[0])