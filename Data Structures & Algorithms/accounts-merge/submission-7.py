class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    # def get_parent(self, u):
    #     if u!=self.parent[u]:
    #         self.parent[u] = self.get_parent(self.parent[u])
    #     return self.parent[u]
    def get_parent(self, curr):
        if curr != self.parent[curr]:
            self.parent[curr] = self.get_parent(self.parent[curr])
        return self.parent[curr]
    
    def union(self, u, v):
        pu, pv = self.get_parent(u), self.get_parent(v)
        if pu==pv:
            return
        
        ru, rv = self.rank[pu], self.rank[pv]
        if ru > rv:
            self.parent[pv] = pu
        elif rv > ru:
            self.parent[pu] = pv
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
            
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 1. Sort the emails first
        accountIdToMailMap = {}
        for i in range(len(accounts)):
            accountIdToMailMap[i] = sorted(accounts[i][1:])
        print(accountIdToMailMap)

        # 2. Create a DSU
        dsu = DSU(len(accounts))

        total_mails = {}
        for id, mail_list in accountIdToMailMap.items():
            for mail in mail_list:
                if mail in total_mails:
                    # We have already seen this mail somewhere,
                    # it means we should merge the 2 accounts
                    prev_mail_user_id = total_mails[mail]
                    dsu.union(prev_mail_user_id, id)
                    # break
                total_mails[mail] = id
        
        print(dsu.parent)
        root_to_emails = defaultdict(set)

        # collect emails by root parent
        for idx in range(len(accounts)):
            root = dsu.get_parent(idx)
            print('parent of',idx, 'is',root)
            root_to_emails[root].update(accountIdToMailMap[idx])

        print(root_to_emails)
        # build final answer
        final_ans = []
        for root, emails in root_to_emails.items():
            name = accounts[root][0]
            merged = [name] + sorted(emails)
            final_ans.append(merged)

        return final_ans

