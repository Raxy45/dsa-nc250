class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
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
                print(w1[j], w2[j])
                if w1[j] != w2[j]:
                    # different char encountered
                    graph[w1[j]].append(w2[j])
                    indegree[w2[j]] += 1
                    break
        
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
        return ans