# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_index = 0
        self.inorder_index = {val:idx for idx, val in enumerate(inorder)}

        def construct(left, right):
            if left >= right:
                return None

            current_root_val = preorder[self.pre_index]
            current_root = TreeNode(current_root_val)
            self.pre_index += 1

            root_index_in_inorder = self.inorder_index[current_root_val]

            current_root.left = construct(left, root_index_in_inorder)
            current_root.right = construct(root_index_in_inorder+1, right)

            return current_root
        return construct(0, len(preorder))