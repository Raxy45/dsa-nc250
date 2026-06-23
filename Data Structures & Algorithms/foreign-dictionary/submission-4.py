class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        ind = defaultdict(int)

        for word in words:
            for c in word:
                ind[c] = 0
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            for j in range(len(w1)):
                if j == len(w2):
                    print(w1, w2)
                    return ""
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    ind[w2[j]] += 1
                    break
        q = deque([])
        for char in ind:
            if ind[char] == 0:
                q.append(char)
        print(graph, ind)
        ans = ""
        while q:
            popped_c = q.popleft()
            ans += popped_c
            for nei in graph[popped_c]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    q.append(nei)
        return ans