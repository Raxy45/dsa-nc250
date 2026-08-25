class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])

        minHeap = []  # pair of [end, numPassengers]
        curPass = 0

        for numPass, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                curPass -= heapq.heappop(minHeap)[1]

            curPass += numPass
            if curPass > capacity:
                return False

            heapq.heappush(minHeap, [end, numPass])

        return True
        
class Solution2:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t:t[1])
        ctp = 0
        hp = []
        for trip in trips:
            curr_pass, st, end = trip

            while hp and st >= hp[0][0]:
                # people are sitting in car & there exists passenger(s) in car, whose end is less than
                # start of current trip. eg: passenger trip ends at 4 (3 pass) and current trip start
                # is 5, then drop the passenger whose trip ends at 4
                _, trip_ended_pass = heapq.heappop(hp)
                ctp -= trip_ended_pass
            
            ctp += curr_pass
            if ctp > capacity:
                return False
            heapq.heappush(hp, (end, curr_pass))
        return True