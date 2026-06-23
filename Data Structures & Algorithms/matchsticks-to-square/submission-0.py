class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False

        sides = [0] * 4

        def dfs(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]

            for side in range(4):
                sides[side] += matchsticks[i]
                if dfs(i + 1):
                    return True
                sides[side] -= matchsticks[i]

            return False

        return dfs(0)