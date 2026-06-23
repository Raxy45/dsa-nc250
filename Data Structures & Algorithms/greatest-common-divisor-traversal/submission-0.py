class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

    def isConnected(self):
        return self.n==1
    
    def find(self, node):
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        p_u, p_v = self.parent[u], self.parent[v]
        if p_u == p_v:
            return False
        
        self.n -= 1
        r_u, r_v = self.rank[p_u], self.rank[p_v]
        if r_u == r_v:
            self.parent[p_u] = p_v
            self.rank[p_v] += 1
        elif r_u > r_v:
            self.parent[p_v] = p_u
        else:
            self.parent[p_u] = p_v
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = DSU(len(nums))
        factor_index_map = {}
        for i, num in enumerate(nums):
            f = 2
            while f*f <= num:
                if (num%f) == 0:
                    if f in factor_index_map:
                        uf.union(i, factor_index_map[f])
                    else:
                        factor_index_map[f] = i
                while num%f == 0:
                    num = num//f
                f += 1
            
            if num>1:
                if num in factor_index_map:
                    uf.union(i, factor_index_map[num])
                else:
                    factor_index_map[num] = i
        return uf.isConnected()