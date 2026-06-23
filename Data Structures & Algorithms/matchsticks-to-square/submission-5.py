class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if (sum(matchsticks)%4)>0 and max(matchsticks)>(sum(matchsticks)/4): return False
        matchsticks.sort()
        print(matchsticks)
        return True