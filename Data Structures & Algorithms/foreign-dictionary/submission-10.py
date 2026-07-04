class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        unique = set()
        for w in words:
            for i in w:
                unique.add(i)
        indegree = {c: 0 for c in unique}
        for i in range(1, len(words)):
            wa, wb = words[i-1], words[i]
            wc = 0
            if len(wa) > len(wb) and wa.startswith(wb):
                return ""
            while wc<len(wa):
                if wc==len(wb):
                    return ""
                if wa[wc] == wb[wc]:
                    wc += 1
                    continue
                # Found mismatch
                # print('hh', graph, wc)
                pre, post = wa[wc], wb[wc]
                if pre in graph and post in graph:
                    if post in set(graph[pre]): return ""
                    break # cause sequence is alread valid, no need to do anything
                # print(graph[post])
                if post not in graph[pre]:
                    graph[pre].add(post)
                    indegree[post] += 1
                break
        ans = ""
        q = deque([])
        for char in indegree:
            if indegree[char] == 0: 
                q.append(char)
        print(indegree, graph)
        while q:
            curr_char = q.popleft()
            del indegree[curr_char]
            ans += curr_char
            dependents = graph[curr_char]
            for nei in dependents:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        print(ans, indegree, graph)
        return ans if len(indegree) == 0 else ""


        # iterate over the unique and find the chars which are not present in visited, add to q
        # now pop elem from q, add to ans. elem is written so which ever nodes have elem as dependency
        # remove elem from their list, if the node's degree become 0, add to q. repeat till q is not empty
                