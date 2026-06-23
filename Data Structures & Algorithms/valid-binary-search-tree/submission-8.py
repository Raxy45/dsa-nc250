# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, lower, upper):
            if not node: return True

            if not (node.val>lower and node.val<upper):
                return False
            
            return (valid(node.left, lower, node.val) and 
                    valid(node.right, node.val, upper))

        return valid(root, float('-inf'), float('inf'))


        # def dfs(node, lower, upper):
        #     if not node: return True

        #     if node.val <= lower or node.val>=upper:
        #         return False
            
        #     # node.val > lower and node.val < upper
        #     if node.left:
        #         # upper = max(upper, node.val)
        #         # lower = min(lower, node.val)
        #         if not dfs(node.left, lower, node.val): return False
            
        #     if node.right:
        #         # upper = max(upper, node.val)
        #         # lower = min(lower, node.val)
        #         if not dfs(node.ri0ght, node.val, upper): return False
        #     return True
        # return dfs(root, -1001, 1001)
            