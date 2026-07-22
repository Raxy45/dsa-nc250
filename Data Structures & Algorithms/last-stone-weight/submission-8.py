class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = [-s for s in stones]
        heapq.heapify(hp)
        while len(hp) > 1:
            a, b = -heapq.heappop(hp), -heapq.heappop(hp)
            if a==b: continue
            heapq.heappush(hp, -(abs(a-b)))
        return -hp[0] if hp else 0
