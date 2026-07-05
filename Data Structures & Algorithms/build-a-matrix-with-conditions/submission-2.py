class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def buildMatrixColRow(conditions):
            graph, indegree = {i:[] for i in range(1, k+1)}, {i:0 for i in range(1, k+1)}
            curr_seq = []
            for node, dependency in conditions:
                graph[node].append(dependency)
                indegree[dependency] += 1
            
            q = deque([])
            for node in indegree:
                if indegree[node] == 0:
                    q.append(node)
            
            indx = 0
            while q:
                node = q.popleft()
                curr_seq.append(node)
                for dependent in graph[node]:
                    indegree[dependent] -= 1
                    if indegree[dependent] == 0:
                        q.append(dependent)
            return curr_seq

        row = buildMatrixColRow(rowConditions)
        if len(row) != k: return []
        col = buildMatrixColRow(colConditions)
        if len(row) != k: return []

        ans = [[0] * (k) for _ in range(k)]
        indices = {i:[] for i in range(1, k+1)}
        for i in range(len(row)):
            indices[row[i]].append(i)
        
        for i in range(len(col)):
            indices[col[i]].append(i)

        print(row, col)
        print(indices)
        for number in indices:
            ans[indices[number][0]][indices[number][1]] = number
        return ans
        # Build row matrix
        # Build col matrix

        # when element is same in row matrix and col matrix -> update ans matrix
        # return ans matrix
