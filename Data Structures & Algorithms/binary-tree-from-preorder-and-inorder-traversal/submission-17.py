# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        imp = {}
        for i, v in enumerate(inorder):
            imp[v] = i
        
        idx = 0
        def construct(lhs, rhs):
            nonlocal idx
            # print(idx, idx==len)
            if idx >= len(preorder): return None
            if lhs>=rhs: return None

            crv = preorder[idx]
            node = TreeNode(crv)
            idx += 1
            node.left = construct(lhs, imp[crv])
            node.right = construct(imp[crv]+1, rhs)
            return node
        return construct(0, len(preorder))