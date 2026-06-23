class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, node):
        curr = self.parent[node]
        while curr != self.parent[curr]:
            curr = self.parent[curr]
        
        return curr

    def union(self, u, v):
        p_u, p_v = self.parent[u], self.parent[v]
        if p_u == p_v: return Fakse

        if self.rank[p_u] > self.rank[p_v]:
            self.parent[p_v] = self.find(p_u)
            self.rank[p_u] += self.rank[p_v]
        else:
            self.parent[p_u] = self.find(p_v)
            self.rank[p_u] += self.rank[p_v]
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))
        graph = {}
        for i, data in enumerate(accounts):
            mail_ids = data[1:]
            for mail in mail_ids:
                if mail not in graph:
                    graph[mail] = i
                else:
                    dsu.union(i, graph[mail])
        
        print(graph)
        print(dsu.parent)

        emailGroup = defaultdict(list)  # index of acc -> list of emails
        for e, i in graph.items():
            # who is father of ith account?
            leader = dsu.find(i)
            emailGroup[leader].append(e)
        
        print(emailGroup)
        
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            print(name, sorted(emailGroup[i]))
            res.append([name] + sorted(emailGroup[i]))
        return res
