class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hp, q = [], deque([])
        counter = Counter(tasks)
        for k, v in counter.items():
            hp.append((-v, k))
        heapq.heapify(hp)
        print(hp)
        # return 1
        t = 0
        while q or hp:
            if hp:
                # we have something to process
                freq, task = heapq.heappop(hp)
                t += 1 #processed
                freq += 1
                if freq<0:
                    # meaning still there is some left over of task to process
                    q.append((t+n, freq, task))
                    # the task can be consumed after t+n. ex: 1 is time processed, n=2
                    # you can process this after 1+2 -> 3 seconds(from start)
                
            if not q:
                # this means nothing is present in ROM
                continue
            
            if t>=q[0][0]:
                # we can move items from ROM to RAM(processor)
                _, freq, p = q.popleft()
                heapq.heappush(hp, (freq, p))
            else:
                # this means current time is still less than the time from which we can process elements from q
                if not hp:
                    # we have nothing to process, bring t to q[0][0]
                    t = q[0][0]
        return t