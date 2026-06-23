class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4 > 0: return False

        matchsticks.sort()
        required_length = total_length/4
        used = [False] * len(matchsticks)

        ans, temp = [], []
        def solve(idx, curr):
            if idx == len(matchsticks):
                return True

            for i in range(0, len(matchsticks)):
                print(matchsticks[i], used[i], curr)
                if used[i]: 
                    continue

                if (curr + matchsticks[i]) > required_length:
                    break
                    
                if (curr + matchsticks[i]) <= required_length:
                    used[i] = True
                    return solve(idx+1, curr)
                
            return False

        return solve(0, 0)
                