class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        passenger_in_car = []
        total_passengers_in_car = 0
        for trip in trips:
            curr_pass, start, end = trip
            while passenger_in_car and start >= passenger_in_car[0][0]:
                _, passenger_seated = heapq.heappop(passenger_in_car)
                total_passengers_in_car -= passenger_seated
            
            total_passengers_in_car += curr_pass
            heapq.heappush(passenger_in_car, (end, curr_pass))
            if total_passengers_in_car > capacity:
                return False
            
            # when to push?
        return True 