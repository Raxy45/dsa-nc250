class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for point in points:
            curr_dist = (point[0]**2 + point[1]**2)**0.5
            heapq.heappush(hp, [-curr_dist, point])
            print(hp)
            if len(hp) > k:
                heapq.heappop(hp)
            print(hp)
            print('88')
        ans = []
        for dist, point in hp:
            ans.append(point)
        return ans