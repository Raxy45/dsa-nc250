class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        outdegree, indegree = {}, {}
        for w in words:
            for c in w:
                if c not in indegree:
                    indegree[c] = 0
        

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            # print(w1.startswith(w2))
            if w1.startswith(w2) and len(w1) > len(w2):
                return ""
            
            for idx in range(len(w1)):
                # if idx == len()
                if w1[idx] == w2[idx]:
                    continue
                
                if w1[idx] != w2[idx]:
                    # mismatch here
                    if w1[idx] not in outdegree:
                        outdegree[w1[idx]] = set()
                    if w2[idx] not in outdegree[w1[idx]]:
                        indegree[w2[idx]] += 1
                        outdegree[w1[idx]].add(w2[idx])
                    break

        print(indegree)
        print(outdegree)

        ans = ""
        q = deque()
        for char in indegree:
            if indegree[char] == 0:
                q.append(char)

        while q:
            char = q.popleft()
            ans += char
            if char not in outdegree:
                continue
            for nei in outdegree[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    # all deps resolved
                    q.append(nei)
                    indegree.pop(nei)
        return ans











        graph, indegree = defaultdict(list), defaultdict(int)
        for word in words:
            for c in word:
                indegree[c] = 0
        print(graph, indegree)

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            for j in range(len(w1)):
                if j==len(w2):
                    # meaning abcd, ab -> this is invalid
                    return ""
                # print(w1[j], w2[j])
                if w1[j] != w2[j]:
                    # different char encountered
                    graph[w1[j]].append(w2[j])
                    indegree[w2[j]] += 1
                    break
        print(graph, indegree)
        q = deque([c for c in indegree if indegree[c]==0])
        ans = ""
        while q:
            char = q.popleft()
            ans += char
            for dependent_char in graph[char]:
                indegree[dependent_char] -= 1
                if indegree[dependent_char] == 0:
                    # this char became independent has no deps to resolved
                    q.append(dependent_char)
        if len(indegree) > len(ans): return ""
        # this if detects cycle -> in case of cycle, we will have nodes with >0 indegree still present -> unprocessed nodes -> therefore len(ans)< total chars [len(indegree)]
        return ans