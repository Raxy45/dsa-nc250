class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4 > 0: return False
        sides = [0] * 4

        required_length = total_length/4
        def dfs(idx):
            if idx == len(matchsticks): return True

            for i in range(4):
                if (sides[i] + matchsticks[idx]) > required_length:
                    break
                
                sides[i] += matchsticks[idx]
                if dfs(idx+1): return True
                sides[i] -= matchsticks[idx]
            return False
        return dfs(0)