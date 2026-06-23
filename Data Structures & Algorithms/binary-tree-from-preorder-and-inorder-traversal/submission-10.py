# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_idx = 0  # pointer in preorder
        # This preorder index is a global variable and it will move from 0 to n, till your recursion call exits

        # Map value -> index in inorder
        self.inorder_index = {val:idx for idx, val in enumerate(inorder)}

        def construct(left, right):
            # left, right are inorder boundaries (inclusive-exclusive)
            # This condition is when you have left == right
            if left == right:
                return None

            # root comes from preorder
            # This is easy part, just determining root of current split
            current_root_val = preorder[self.pre_index]
            current_root = TreeNode(current_root_val)
            self.pre_index += 1

            # split inorder using hashmap
            root_index_in_inorder = self.inorder_index[current_root_val]

            # build left and right subtrees
            # Just a game of index
            current_root.left = construct(left, root_index_in_inorder)
            current_root.right = construct(root_index_in_inorder+1, right)

            return current_root
        return construct(0, len(preorder))