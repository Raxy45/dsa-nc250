class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        q = list(zip(capital, profits))
        print(q)
        q.sort()
        q = deque(q)
        print(q)
        hp = []

        for i in range(1, k+1):
            # print('Going to do project', i)
            # print('Current capital', w)
            while q and w>=q[0][0]:
                proj_cap, proj_prof = q.popleft()
                heapq.heappush(hp, (-proj_prof, proj_cap))

            # print('list of projects indentified', hp)
            if not hp:
                return w
            
            max_prof_proj, proj_cap = heapq.heappop(hp)
            w += (-max_prof_proj)
        return w