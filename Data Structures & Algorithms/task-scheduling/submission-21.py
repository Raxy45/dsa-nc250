class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounter = Counter(tasks)
        hp = [(-f, task) for task, f in taskCounter.items()]
        heapq.heapify(hp)
        cooldown = deque([])
        t = 0
        while hp:
            freq, task = heapq.heappop(hp)
            freq += 1
            t += 1
            # print('did ',task, 'updated time and freq', t, freq)
            # print('B4', hp, cooldown)
            if freq!=0:
                cooldown.append((t+n, freq, task))
            
            while cooldown and t == cooldown[0][0]:
                _, cooled_freq, task = cooldown.popleft()
                heapq.heappush(hp, (cooled_freq, task))
            
            if not hp and cooldown:
                t, cooled_freq, task = cooldown.popleft()
                heapq.heappush(hp, (cooled_freq, task))
            # print('Aftter', hp, cooldown)
            # print(',,,')
        return t

        