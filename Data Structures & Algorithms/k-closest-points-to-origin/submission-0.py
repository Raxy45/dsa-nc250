class Node:
    def __init__(self, dist, points):
        self.dist = dist
        self.ps = points
    
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        ans = []
        add = True
        dist_dict = {}
        for point in points:
            x, y = point[0], point[1]
            dist = x**2 + y**2
            heapq.heappush(min_heap, (-dist, x, y))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        print(min_heap)
        while min_heap:
            popped = heapq.heappop(min_heap)
            ans.append([popped[1], popped[2]])
        print(ans)
        return ans