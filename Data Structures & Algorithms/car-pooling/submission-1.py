class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        hp = []
        trips.sort(key=lambda t:t[1])

        curr_trip_passenger = 0
        for trip in trips:
            n_pass, start, end = trip
            while hp and start>=hp[0][0]:
                curr_trip_passenger -= hp[0][1]
                heapq.heappop(hp)
                
            curr_trip_passenger += n_pass
            if curr_trip_passenger > capacity: return False

            heapq.heappush(hp, (end, n_pass))
        return True
            
            