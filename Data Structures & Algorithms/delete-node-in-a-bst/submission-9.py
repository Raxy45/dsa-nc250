# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        
        # root.val == key
        if root.left and not root.right:
            return root.left
        elif root.right and not root.left:
            return root.right
        elif not root.left and not root.right:
            # leaf node
            return None
        
        right_child = root.right
        while right_child.left:
            right_child = right_child.left
        
        root.val = right_child.val
        root.right = self.deleteNode(root.right, root.val)
        return root