# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: idx for idx, val in enumerate(inorder)}
        self.pre_index = 0

        def construct(left, right):
            if left>=right: return None

            root_val = preorder[self.pre_index]
            self.pre_index += 1
            root = TreeNode(root.val)

            mid = inorder_idx[root_val]

            root.left = construct(left, mid)
            root.right = construct(mid+1, right)
            return root
        return construct(0, len(inorder))
