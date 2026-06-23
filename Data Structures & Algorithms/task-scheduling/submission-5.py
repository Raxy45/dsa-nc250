class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        char_count = Counter(tasks)
        hp = [-count for count in char_count.values()]
        heapq.heapify(hp)
        time = 0
        while hp or q:
            time += 1
            print(time, hp, q)
            if not hp:
                time = q[0][0]
            else:
                freq= heapq.heappop(hp)
                freq += 1
                if freq==0: continue
                q.append((time+n, freq))
            if q and time == q[0][0]:
                heapq.heappush(hp, q[0][1])
                q.popleft()
        return time