class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [1] * n
            
            def find(self, curr):
                if self.parent[curr] != curr:
                    self.parent[curr] = self.find(self.parent[curr])
                return self.parent[curr]
            
            def union(self, u, v):
                p_u, p_v = self.find(u), self.find(v)
                if p_u == p_v:
                    return
                
                r_u, r_v = self.rank[p_u], self.rank[p_v]
                if r_v > r_u:
                    self.parent[p_u] = p_v
                elif r_u > r_v:
                    self.parent[p_v] = p_u
                else:
                    self.parent[p_u] = p_v
                    self.rank[p_v] += 1


        dsu = DSU(len(accounts))
        mail_graph = defaultdict(list)
        account_idx_mail_map = defaultdict(list)
        for idx, account in enumerate(accounts):
            name = account[0]
            account_idx_mail_map[idx] = account[1:]
            for mail_id in account[1:]:
                mail_graph[mail_id].append(idx)
        print(mail_graph)
        print(account_idx_mail_map)

        print(dsu.parent)
        for mail, account_list in mail_graph.items():
            if len(account_list) == 1:
                continue
            for i in range(len(account_list)-1):
                u = account_list[i]
                v = account_list[i+1]
                dsu.union(u, v)
        
        print(dsu.parent)
        final_ans = []
        
        root_to_emails = defaultdict(set)

        # collect emails by root parent
        for idx in range(len(accounts)):
            root = dsu.find(idx)
            print('parent of',idx, 'is',root)
            root_to_emails[root].update(account_idx_mail_map[idx])

        print(root_to_emails)
        # build final answer
        final_ans = []
        for root, emails in root_to_emails.items():
            name = accounts[root][0]
            merged = [name] + sorted(emails)
            final_ans.append(merged)

        return final_ans
