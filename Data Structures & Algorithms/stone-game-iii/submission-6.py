class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        stone = stoneValue
        n = len(stoneValue)
        def solve(i):
            if i>=n:
                return 0
            
            curr = stone[i] - solve(i+1)
            if (i+1)<n:
                curr = max(curr, stone[i]+stone[i+1] - solve(i+2))
            
            if (i+2)<n:
                curr = max(curr, stone[i]+stone[i+1]+stone[i+2] - solve(i+3))
            return curr
        
        ans = solve(0)
        if ans == 0:
            return "Tie"
        if ans>0:
            return "Alice"
        return "Bob"