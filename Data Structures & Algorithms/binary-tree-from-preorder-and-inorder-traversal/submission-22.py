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
        

        r_idx = 0
        def dfs(l, r):
            nonlocal r_idx
            # print(r_idx, l, r)
            if l>r or l<0 or r>=(len(inorder)) or r_idx >= len(inorder):
                # print('returning none')
                return None
            if l==r:
                # print('Constructing for single elem ', preorder[r_idx])
                return TreeNode(preorder[r_idx])
            
            root_val = preorder[r_idx]
            # print('constructing node for', root_val, l, r)
            root = TreeNode(root_val)
            r_idx += 1
            
            root.left = dfs(l, iomp[root_val] - 1)
            if root.left:
                r_idx += 1

            # print('Calling for', r_idx ,'for',root_val)
            root.right = dfs(iomp[root_val] + 1, r)
            return root
        return dfs(0, len(inorder)-1)
        