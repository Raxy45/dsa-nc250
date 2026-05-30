class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hp, q = [], deque([])
        tasks = Counter(tasks)
        for k, v in tasks.items():
            hp.append((-v, k))
        print(hp)
        heapq.heapify(hp)
        t = 0
        d = 0
        while hp or q:
            if hp:
                n_tasks, popped_task = heapq.heappop(hp)
                n_tasks += 1
                t += 1
                if n_tasks<0: 
                    q.append((t+n, n_tasks, popped_task))
                
                # can be consumed after t+n
            
            # print(t, q[0][0], 'why not')
            # use only q, heap is exhausted
            if not q: continue
            if t == q[0][0]:
                # cooldown of task in q is over, add to heap
                time, freq, p = q.popleft()
                # print('cooldown of task in q is over, add to heap', time, freq, p)
                heapq.heappush(hp, (freq, p))
            else:
                # current time is less than the cooldown timing in q[0]
                # print('# current time is less than the cooldown timing in q[0]')
                if not hp:
                    # but we have no elements left to process in hp, therefore bring time to q[0]
                    t = q[0][0]
                    # print('# but we have no elements left to process in hp, therefore bring time to q[0]', t)
            # print('*****')
        return t
            
