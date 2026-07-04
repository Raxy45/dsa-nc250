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
        for i in range(1, len(words)):
            wa, wb = words[i-1], words[i]
            wc = 0
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
                if pre not in graph[post]:
                    graph[post].add(pre)
                    break
            # print(graph)
            if wc == len(wb) and wc<len(wa): return ""
        ans = ""
        q = deque([])
        for char in unique:
            if char not in graph: q.append(char)
        # print(q, graph)
        # return ""
        while q:
            curr_char = q.popleft()
            ans += curr_char
            temp = graph.copy()
            for key in temp:
                if curr_char in temp[key]: 
                    graph[key].remove(curr_char)
                if len(temp[key]) == 0:
                    q.append(key)
                    del graph[key]
        return ans if len(graph) == 0 else ""


        # iterate over the unique and find the chars which are not present in visited, add to q
        # now pop elem from q, add to ans. elem is written so which ever nodes have elem as dependency
        # remove elem from their list, if the node's degree become 0, add to q. repeat till q is not empty
                