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
        return curr
    
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
                    break
                total_mails[mail] = id
        
        print(dsu.parent)
        temp = {}
        for id in range(len(accounts)):
            print(id, temp)
            if dsu.parent[id] != id:
                # merge the two group of mail ids
                # original account id(id) & the parent of account id(dsu.parent[id])
                prev_mail_ids = temp.get(dsu.parent[id], [])
                print(prev_mail_ids)
                prev_mail_ids.extend(accountIdToMailMap[id])
            else:
                temp[id] = accountIdToMailMap[id]
        ans = []
        for id, merged_mail_list in temp.items():
            print(id, merged_mail_list)
            current = [accounts[id][0]] # name
            current.extend(sorted(set(merged_mail_list)))
            ans.append(current)
        # print('ans', ans)
        return ans

