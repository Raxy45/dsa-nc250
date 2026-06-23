class Solution:
    def findItinerary(self, tickets):
        tickets.sort()
        visited = [False]*len(tickets)
        path = ["JFK"]

        def dfs(curr):
            if len(path) == len(tickets) + 1:
                return True

            for i in range(len(tickets)):
                src, dst = tickets[i]

                if src == curr and not visited[i]:
                    visited[i] = True
                    path.append(dst)

                    if dfs(dst):
                        return True

                    path.pop()
                    visited[i] = False

            return False

        dfs("JFK")
        return path