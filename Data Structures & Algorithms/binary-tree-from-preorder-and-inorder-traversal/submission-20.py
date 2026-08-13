# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        iomp = {}
        for i in range(len(inorder)):
            iomp[inorder[i]] = i
        

        def dfs(r_idx, l, r):
            if l==r:
                return TreeNode(inorder[l])
            if l>r or l<0 or r>=(len(inorder)):
                return None
            
            root_val = preorder[r_idx]
            root = TreeNode(root_val)

            r_idx += 1
            root.left = dfs(r_idx, l, iomp[root_val] - 1)

            r_idx += 1
            root.right = dfs(r_idx, iomp[root_val] + 1, r)
            return root
        return dfs(0, 0, len(inorder)-1)
        