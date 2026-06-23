class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = Counter(tasks)
        hp, q = [], deque()
        for task, freq in task_freq.items():
            heapq.heappush(hp, (-freq, task))
        time = 0
        while q or hp:
            print(hp, q, time)
            if hp:
                freq, popped_task = heapq.heappop(hp)
                freq += 1
                if freq != 0:
                    q.append((time+n, (freq, popped_task)))
            if q and time >= q[0][0]:
                heapq.heappush(hp, q.popleft()[1])
            time += 1
        return time