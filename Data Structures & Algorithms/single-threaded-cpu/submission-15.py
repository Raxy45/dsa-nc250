class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        updated_tasks = deque()
        for idx, (enq, proc) in enumerate(tasks):
            updated_tasks.append([enq, idx, proc])

        updated_tasks = deque(sorted(updated_tasks, key=lambda x: x[0]))
        print(updated_tasks)
        ans = []
        q, hp = deque([updated_tasks[0]]), []
        time = updated_tasks[0][0]
        counter = 0
        while updated_tasks:
            print(time, updated_tasks)
            while updated_tasks and time >= updated_tasks[0][0]:
                _, idx, p_time = updated_tasks.popleft()
                heapq.heappush(hp, (p_time, idx))
            
            while hp:
                p_time, idx = heapq.heappop(hp)
                print(idx, p_time)
                ans.append(idx)
                time += p_time
            print('actual time', time)
            if updated_tasks and time<updated_tasks[0][0]:
                time = updated_tasks[0][0]
        return ans
