class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_meter = [0] * (n+1)
        vote_count = defaultdict(int)
        for person in trust:
            trust_meter[person[0]] = 1
            vote_count[person[1]] += 1
        for i in range(1,n+1):
            if trust_meter[i] == 0 and vote_count[i]==n-1: return i

        return -1