class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        passenger_in_car = []
        total_passengers_in_car = 0
        for trip in trips:
            curr_pass, start, end = trip
            # before adding check if passengers already seated in car. Someone's end journey(eg: 10) <= start journey of current(eg: 15)
            # then in such case, the passenger seating in car should be removed.
            while passenger_in_car and start >= passenger_in_car[0][0]:
                _, passenger_seated = heapq.heappop(passenger_in_car)
                total_passengers_in_car -= passenger_seated
            

            # You are always going to add the current number of passengers in total
            total_passengers_in_car += curr_pass
            heapq.heappush(passenger_in_car, (end, curr_pass))
            if total_passengers_in_car > capacity:
                # if at any given point total passengers > capacity -> pop them out
                return False
            
        return True 