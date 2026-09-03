class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        outdegree, indegree = {}, {}

        # Every character is a node
        for w in words:
            for c in w:
                indegree[c] = 0

        # Build graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # Invalid case: longer word comes before its prefix
            if w1.startswith(w2) and len(w1) > len(w2):
                return ""

            # Only first mismatch matters
            for idx in range(min(len(w1), len(w2))):
                if w1[idx] == w2[idx]:
                    continue

                u, v = w1[idx], w2[idx]

                if u not in outdegree:
                    outdegree[u] = set()

                # Avoid duplicate edge
                if v not in outdegree[u]:
                    outdegree[u].add(v)
                    indegree[v] += 1

                break

        # Topological sort
        q = deque()

        for char in indegree:
            if indegree[char] == 0:
                q.append(char)

        ans = ""

        while q:
            char = q.popleft()
            ans += char

            for nei in outdegree.get(char, []):
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        # Cycle detection
        return ans if len(ans) == len(indegree) else ""