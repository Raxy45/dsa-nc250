class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dest in tickets:
            graph[src].append(dest)
        print(graph)

        q = deque()
        visited = [0]*len(tickets)
        ans = []

        def dfs(src):
            nonlocal ans
            q.append(src)
            for dest in graph[src]:
                if (src, dest) not in visited:
                    visited.add((src, dest))
                    if dfs(dest):
                        ans.append(list(q))
                        print('found',q)
                        print('ans', ans)
                    visited.remove((src, dest))
                    q.pop()

            return len(visited) == len(tickets)
        dfs('JFK')
        print(ans)
        return sorted(list(ans))[0]
