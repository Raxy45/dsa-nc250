class DSU:
    def __init__(self, n):
        self.n = n
        self.rank = [0] * n
        self.p = [i for i in range(n)]

    def find(self, node):
        if node != self.p[node]:
            self.p[node] = self.find(self.p[node])
        return self.p[node]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu==pv: return

        ru, rv = self.rank[pu], self.rank[pv]
        if ru==rv:
            self.p[pv] = pu
            self.rank[pu] += 1
        elif ru>rv:
            self.p[pv] = pu
        else:
            self.p[pu] = pv
        self.n -= 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        dsu = DSU(len(nums))

        def get_factors(n, idx):
            # factors = set()
            i = 2
            while i * i <= n:
                if (n%i) == 0:
                    if i in factors_to_idx:
                        dsu.union(idx, factors_to_idx[i])
                    else:
                        factors_to_idx[i] = idx
                    # factors.add(i)
                    n = int(n/i)
                    continue
                i  += 1
            if n>1:
                if n in factors_to_idx:
                    dsu.union(idx, factors_to_idx[n])
                else:
                    factors_to_idx[n] = idx
            
        factors_to_idx = {}
        for i in range(len(nums)):
            get_factors(nums[i], i)
        return dsu.n==1