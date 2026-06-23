class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        updated_tasks = deque()
        for idx, (enq, proc) in enumerate(tasks):
            updated_tasks.append([enq, idx, proc])

        updated_tasks = deque(sorted(updated_tasks, key=lambda x: x[0]))
        
        ans = []
        hp = []
        time = updated_tasks[0][0]
        while updated_tasks or hp:
            while updated_tasks and time >= updated_tasks[0][0]:
                _, idx, p_time = updated_tasks.popleft()
                heapq.heappush(hp, (p_time, idx))
            
            if hp:
                p_time, idx = heapq.heappop(hp)
                ans.append(idx)
                time += p_time
                if updated_tasks and time<updated_tasks[0][0]:
                    time = updated_tasks[0][0]
        return ans
