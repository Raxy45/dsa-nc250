class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ut = []
        for p, s, e in trips:
            ut.append((s, e, p))
        ut.sort()

        q = deque(ut)
        hp = []
        pass_total = 0
        while hp or q:
            if not hp:
                # no trip picked up yet
                _, end, ctp = q.popleft()
                pass_total += ctp
                heapq.heappush(hp, (end, ctp))
            
            while q and hp and q[0][0] < hp[0][0]:
                _, end, ctp = q.popleft()
                pass_total += ctp
                if pass_total > capacity:
                    return False
                heapq.heappush(hp, (end, ctp))
            
            while hp:
                _, ctp = heapq.heappop(hp)
                pass_total -= ctp
        return True