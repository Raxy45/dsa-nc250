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
        
                

        # for idx, mails in account_name_mail_map.items():
        #     temp = []
        #     account_name = accounts[idx][0]
        #     temp.append(account_name)
        #     if idx != dsu.parent[idx]:
        #         temp.extend(account_name_mail_map[dsu.parent[idx]])
        #     temp.append(mails)
        #     final_ans.append(temp)
        print(final_ans)
        return final_ans
