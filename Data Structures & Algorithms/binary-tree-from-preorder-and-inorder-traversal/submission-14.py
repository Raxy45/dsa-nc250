# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val:idx for idx, val in enumerate(inorder)}
        preorder_index = 0
        def construct(start, end):
            nonlocal preorder_index
            if start==end: return None
            
            current_root_val = preorder[preorder_index]
            current_root = TreeNode(current_root_val)
            preorder_index += 1
            current_root.left = construct(start, inorder_map[current_root_val])
            current_root.right = construct(inorder_map[current_root_val]+1, end)
            return current_root
        return construct(0, len(preorder))