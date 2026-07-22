class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for i, [x, y] in enumerate(points):
            print(x, y, x**2 + y**2)
            heapq.heappush(hp, (-(x**2 + y**2), i))
            if len(hp) > k:
                heapq.heappop(hp)
        return [points[i] for _, i in hp]