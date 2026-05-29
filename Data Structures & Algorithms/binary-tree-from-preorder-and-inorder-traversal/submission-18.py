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
            print(i, v)
            imp[v] = i
        
        idx = 0
        def construct(lhs, rhs):
            nonlocal idx
            if idx == len(inorder) or lhs==rhs: return None

            crv = preorder[idx]
            node = TreeNode(crv)
            # I have created node for me, now i will point to
            # the next root index

            idx += 1
            node.left = construct(lhs, imp[crv])
            node.right = construct(imp[crv]+1, rhs)
            return node

        return construct(0, len(inorder))