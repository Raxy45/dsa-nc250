"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        R, C = len(grid), len(grid[0])

        def dfs(ur, uc, er, ec):
            # print('Starting for', ur, uc, er, ec)
            node = Node(grid[ur][uc], True)
            for i in range(ur, er):
                for j in range(uc, ec):
                    # print('current', i, j)
                    if j<ec-1 and grid[i][j] != grid[i][j+1] \
                    or i<er-1 and grid[i][j] != grid[i+1][j]:
                        # print('Calling for', i, j, 'topLeft', ur,uc,er,ec)
                        node.topLeft = dfs(ur, uc, (ur+er)//2, (uc+ec)//2)

                        # print('Calling for', i, j, 'topRight')
                        node.topRight = dfs(ur, (uc+ec)//2, (ur+er)//2, ec)
#
                        # print('Calling for', i, j, 'bottomLeft')
                        node.bottomLeft = dfs((ur+er)//2, uc, er, (uc+ec)//2)

                        # print('Calling for', i, j, 'bottomRight')
                        node.bottomRight = dfs((ur+er)//2, (uc+ec)//2, er, ec)
                        node.isLeaf = False
                        return node
            # print('***')
            return node
            

        
        for r in range(R):
            for c in range(C):
                if c<C-1 and grid[r][c] != grid[r][c+1]:
                    return dfs(0, 0, R, C)
                    
        return Node(grid[0][0], True, None, None, None, None)