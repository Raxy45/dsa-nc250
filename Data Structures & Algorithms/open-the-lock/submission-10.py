class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        current = '0000'
        deadends = set(deadends)
        steps = 0
        
        q = deque([('0000', 0)])
        def get_next(num, dir):
            updated = int(num)+dir+10
            return str(updated%10)
                
        while q:
            curr, steps = q.popleft()
            if curr == target: return steps
            if curr in deadends: continue
            deadends.add(curr)
            for i in range(4):
                plus_one = curr[:i]+get_next(curr[i], +1)+curr[i+1:]
                if plus_one not in deadends: q.append((plus_one, steps+1))

                minus_one = curr[:i]+get_next(curr[i], -1)+curr[i+1:]
                if minus_one not in deadends: q.append((minus_one, steps+1))
        return -1




            
