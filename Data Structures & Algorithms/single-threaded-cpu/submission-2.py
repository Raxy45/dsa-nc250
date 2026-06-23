class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_idx_map = defaultdict()
        for idx, task in enumerate(tasks):
            task_idx_map[tuple(task)] = idx
        
        print(tasks)
        tasks.sort()
        print(tasks)
        
        q, hp = deque(tasks), []
        time, ans = tasks[0][0], []
        while q or hp:
            # print('q', q)
            # print('time', time)
            # print('hp', hp)
            while q and time >= q[0][0]:
                heapq.heappush(hp, (q[0][1], q[0]))
                q.popleft()

            # print('after getting eligible tasks')
            # print('q', q)
            # print('hp', hp)
            # process hp if task exists in hp
            if hp:
                task_time, popped_task = heapq.heappop(hp)
                time += task_time
                ans.append(task_idx_map[tuple(popped_task)])
            else:
                time += 1
            # print('*'*10)
        return ans