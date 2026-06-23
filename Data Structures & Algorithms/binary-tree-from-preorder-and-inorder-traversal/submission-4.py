# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map value -> index in inorder
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        
        self.pre_idx = 0  # pointer in preorder

        def construct(left, right):
            # left, right are inorder boundaries (inclusive-exclusive)
            if left >= right:
                return None

            # root comes from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # split inorder using hashmap
            mid = inorder_index[root_val]

            # build left and right subtrees
            root.left = construct(left, mid)
            root.right = construct(mid + 1, right)

            return root

        return construct(0, len(inorder))
