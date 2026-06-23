class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_map = defaultdict(int)
        trust_count = defaultdict(int)
        for person, trusted_person in trust:
            trust_map[person] = trusted_person
            trust_count[trusted_person] += 1
        
        for i in range(1, n+1):
            if i not in trust_map:
                # chances are he can be judge
                if trust_count[i] == n-1: return i
        return -1