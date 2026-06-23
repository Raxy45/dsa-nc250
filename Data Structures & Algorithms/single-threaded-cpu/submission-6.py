class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        updated_tasks = []
        for idx, task in enumerate(tasks):
            updated_tasks.append((task[0], task[1], idx))
        print(updated_tasks)
        updated_tasks.sort()
        print(updated_tasks)
        
        q, hp = deque(updated_tasks), []
        time, ans = updated_tasks[0][0], []
        while q or hp:
            # print('q', q)
            # print('time', time)
            # print('hp', hp)
            while q and time >= q[0][0]:
                heapq.heappush(hp, (q[0][1], q[0][2]))
                q.popleft()

            # print('after getting eligible tasks')
            # print('q', q)
            # print('hp', hp)
            # process hp if task exists in hp
            if hp:
                task_time, popped_task_index = heapq.heappop(hp)
                time += task_time
                ans.append(popped_task_index)
            else:
                time += 1
            # print('*'*10)
        return ans

    def getOrderv1(self, tasks: List[List[int]]) -> List[int]:
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
                heapq.heappush(hp, (q[0][1], task_idx_map[tuple(q[0])]))
                q.popleft()

            # print('after getting eligible tasks')
            # print('q', q)
            # print('hp', hp)
            # process hp if task exists in hp
            if hp:
                task_time, popped_task_index = heapq.heappop(hp)
                time += task_time
                ans.append(popped_task_index)
            else:
                time += 1
            # print('*'*10)
        return ans