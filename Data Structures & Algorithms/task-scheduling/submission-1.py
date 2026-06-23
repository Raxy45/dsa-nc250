class Solution:
    def leastInterval(self, tasks: List[str], p: int) -> int:
        n = len(tasks)
        freq_map = Counter(tasks)

        # max heap using negative frequencies
        pq = []
        for freq in freq_map.values():
            heapq.heappush(pq, -freq)

        time = 0

        while pq:
            temp = []

            # fill p+1 slots
            for _ in range(p + 1):
                if pq:
                    freq = heapq.heappop(pq) + 1  # execute once
                    temp.append(freq)

            # push remaining frequencies back
            for freq in temp:
                if freq > 0:
                    heapq.heappush(pq, -freq)

            # update time
            if not pq:
                time += len(temp)
            else:
                time += (p + 1)

        return time