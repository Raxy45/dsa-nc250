class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for point in points:
            x, y = point[0], point[1]
            dist = (x**2 + y**2)**0.5
            heapq.heappush(hp, (-dist, point))
            if len(hp) > k:
                heapq.heappop(hp)
            
        return [p[1] for p in hp]
