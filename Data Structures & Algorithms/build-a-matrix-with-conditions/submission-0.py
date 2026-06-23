class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_g, col_g = defaultdict(list), defaultdict(list)
        row_ind, col_ind = {i:0 for i in range(1, k+1)}, {i:0 for i in range(1, k+1)}

        for u, v in rowConditions:
            # u must come before v
            # edge u -> v
            # aka v depends on u
            row_ind[v] += 1
            row_g[u].append(v) # because when you process node with ind 0 -> you will have to let indegree of v reduce by 1 
            # because a node(u) having arrow towards v, has been processed therefore decrease indegree of v by one

        for u, v in colConditions:
            col_ind[v] += 1
            col_g[u].append(v)
        
        # print(row_g, col_g)
        row_q, col_q = deque([]), deque([])
        for node, ind in row_ind.items():
            if ind==0:
                row_q.append(node)
        
        for node, ind in col_ind.items():
            if ind==0:
                col_q.append(node)

        col_indx, row_indx = [], []
        # print(row_q)
        while row_q:
            node = row_q.popleft()
            row_indx.append(node)

            for nei in row_g[node]:
                row_ind[nei] -= 1
                if row_ind[nei] == 0:
                    row_q.append(nei)
        # print(row_indx)
        if len(row_indx)<k: return []

        while col_q:
            node = col_q.popleft()
            col_indx.append(node)

            for nei in col_g[node]: 
                col_ind[nei] -= 1
                if col_ind[nei] == 0:
                    col_q.append(nei)

        if len(col_indx) < k: return []
        
        matrix_cord = {i:[-1, -1] for i in range(1, k+1)}
        for i in range(k):
            matrix_cord[row_indx[i]][0] = i
            matrix_cord[col_indx[i]][1] = i
        # print(matrix_cord)

        matrix = [[0 for _ in range(k)] for _ in range(k)]
        for val, (r, c) in matrix_cord.items():
            matrix[r][c] = val
        return matrix
        