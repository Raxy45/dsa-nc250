class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        updated_tasks = deque()
        for idx, (enq, proc) in enumerate(tasks):
            updated_tasks.append([enq, idx, proc])

        updated_tasks = deque(sorted(updated_tasks, key=lambda x: x[0]))
        print(updated_tasks)
        ans = []
        q, hp = deque(), []
        time = updated_tasks[0][0]
        counter = 0
        while updated_tasks or hp:
            while updated_tasks and time >= updated_tasks[0][0]:
                _, idx, p_time = updated_tasks.popleft()
                heapq.heappush(hp, (p_time, idx))
            
            print('hp', hp)
            if hp:
                p_time, idx = heapq.heappop(hp)
                print(idx, p_time)
                ans.append(idx)
                time += p_time
                if updated_tasks and time<updated_tasks[0][0]:
                    time = updated_tasks[0][0]
        return ans
