class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hp, q = [], deque([])
        tasks = Counter(tasks)
        for k, v in tasks.items():
            hp.append((-v, k))
        print(hp)
        heapq.heapify(hp)
        print('after heapify', hp)
        t = 1
        d = 0
        while hp or q:
            d += 1
            if d>500: return 1
            print('time:', t)
            if hp:
                print('in heap')
                n_tasks, popped_task = heapq.heappop(hp)
                print('current tasks remaining', n_tasks,'of', popped_task)
                n_tasks += 1
                if n_tasks==0: 
                    print('tasks completed, SKIPPED ADDING to Q and hp')
                    continue
                print('task can be consumed after', t+n, 'remaining', n_tasks, 'for', popped_task)
                q.append((t+n, n_tasks, popped_task))
                t += 1
                # can be consumed after t+n
            
            # use only q, heap is exhausted
            if t > q[0][0]:
                # cooldown of task in q is over, add to heap
                time, freq, p = q.popleft()
                print('cooldown of task in q is over, add to heap', time, freq, p)
                heapq.heappush(hp, (freq, p))
            else:
                # current time is less than the cooldown timing in q[0]
                print('# current time is less than the cooldown timing in q[0]')
                if not hp:
                    # but we have no elements left to process in hp, therefore bring time to q[0]
                    print('# but we have no elements left to process in hp, therefore bring time to q[0]')
                    t = q[0][0]+1
            # print('IN QUEUE')
            # if q[0][0]<t:
            #     if hp: 
            #         print('heap exists, skipped popping from q')
            #         continue
            #     t = q[0][0]
            # if not hp:
            #     curr_t, freq, p = q.popleft()
            #     print('current t', curr_t, 'freq', freq)
            #     t += 1
            #     print('freq', freq, 'can be consumed after', t+n)
            #     heapq.heappush(hp, (freq, p))
            print('*****')
        return t
            
