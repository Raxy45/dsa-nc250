class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        q = []
        for pas, st, end in trips:
            q.append([st, end, pas])
        
        q.sort()
        q = deque(q)
        q2 = deque()
        t = 0, q[0][0]
        while q:
            _, t, p = q.popleft()
            q2.append([t, p])
            while q and q[0][0] < t:
                new_people_st, n_p_et, n_p = q.popleft()
                q2.append([n_p_et, n_p])
                p += n_p
            if p > capacity:
                return False
            
            while q2 and t>=q2[-1][0]:
                _, removed_p = q2.popleft()
                p -= removed_p
        return True
            
