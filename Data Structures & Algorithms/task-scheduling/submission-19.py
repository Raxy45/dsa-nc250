class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounter = Counter(tasks)
        hp = [-f for task, f in taskCounter.items()]
        heapq.heapify(hp)
        cooldown = deque([])
        t = 0
        while hp:
            freq = heapq.heappop(hp)
            freq += 1
            t += 1
            if freq!=0:
                cooldown.append((t+n, freq))
            
            while cooldown and t == cooldown[0]:
                _, cooled_freq = cooldown.popleft()
                heapq.heappush(hp, cooled_freq)
            
            if not hp and cooldown:
                t, cooled_freq = cooldown.popleft()
                heapq.heappush(hp, cooled_freq)
        return t

        