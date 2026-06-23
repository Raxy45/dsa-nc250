class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Step 1: attach original index
        updated_tasks = []
        for idx, (enqueue, process) in enumerate(tasks):
            updated_tasks.append((enqueue, process, idx))

        # Step 2: sort by enqueue time
        updated_tasks.sort()

        q = deque(updated_tasks)
        hp = []
        ans = []

        # Step 3: initialize time correctly
        time = q[0][0]

        # Step 4: simulation
        while q or hp:
            # add all available tasks to heap
            while q and q[0][0] <= time:
                enqueue, process, idx = q.popleft()
                heapq.heappush(hp, (process, idx))

            if hp:
                process, idx = heapq.heappop(hp)
                time += process
                ans.append(idx)
            else:
                # CPU idle → jump time
                time = q[0][0]

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
            while q and time >= q[0][0]:
                heapq.heappush(hp, (q[0][1], task_idx_map[tuple(q[0])]))
                q.popleft()

            if hp:
                task_time, popped_task_index = heapq.heappop(hp)
                time += task_time
                ans.append(popped_task_index)
            else:
                time += q[0][0]
        return ans