class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        hp = [(-c, char) for char, c in Counter(tasks).items()]
        heapq.heapify(hp)

        time = 0
        while hp or q:
            print(hp, q, time)
            if hp:
                freq, current_task = heapq.heappop(hp)
                freq += 1
                time += 1

                if freq:
                    q.append((time+n, freq, current_task))
            else:
                time += 1

            if q and time==q[0][0]:
                t, freq, char = q.popleft()
                heapq.heappush(hp, (freq, char))
            print('after', hp, q, time)
        return time