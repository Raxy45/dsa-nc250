class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        q, hp = deque([]), []
        for i, (enq, prc) in enumerate(tasks):
            tasks[i].append(i)
        print(tasks, 'sss')
        tasks.sort()
        q = deque(tasks)
        t = q[0][0]
        ans = []
        while q or hp:
            while q and t>=q[0][0]:
                enq, prc, i = q.popleft()
                heapq.heappush(hp, (prc, i))
            
            if hp:
                prc, idx = heapq.heappop(hp)
                t += prc
                ans.append(idx)
        return ans
