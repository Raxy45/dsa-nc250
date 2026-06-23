class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])

        hp = []
        total_pass = 0
        for trip in trips:
            n_pass, start, end = trip
            while hp and start>=hp[0][0]:
                total_pass -= hp[0][1]
                heapq.heappop(hp)
            
            total_pass += n_pass
            heapq.heappush(hp, (end, n_pass))
            if total_pass > capacity: return False
        return True