class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        indegree, outdegree = {}, {}
        max_wl = -1
        for word in words:
            max_wl = max(max_wl, len(word))
        
        idx = 0
        while idx<max_wl:
            # print(idx, 'idx')
            for i in range(1, len(words)):
                w1, w2 = words[i-1], words[i]
                # print(w1, w2)
                if idx == len(w1) or idx ==len(w2) or w1[idx] == w2[idx]:
                    continue
                if w1[idx] not in outdegree:
                    outdegree[w1[idx]] = []
                
                if w2[idx] not in set(outdegree[w1[idx]]):
                    outdegree[w1[idx]].append(w2[idx])
                    if w2[idx] not in indegree:
                        indegree[w2[idx]] = 0
                    indegree[w2[idx]] += 1
            # print(indegree, outdegree)
            idx += 1
                # build indegree and outdegree
        
        # print(indegree)
        # print(outdegree)
        
        q = deque([])
        for char in outdegree:
            if char not in indegree:
                q.append(char)
        
        ans = ""
        while q:
            char = q.popleft()
            ans += char
            if char not in outdegree:
                continue
            for dependent in outdegree[char]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    indegree.pop(dependent)
                    q.append(dependent)
        
        return ans if len(indegree) == 0 else ""