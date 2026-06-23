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
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
        # root.val == key:
            if not root.left and not root.right:
                # this is terminal node simply return None
                return None
            
            if not root.left: return root.right
            if not root.right: return root.left

            left_child = root.left
            while left_child and left_child.right:
                left_child = left_child.right
            
            root.val = left_child.val
            root.left = self.deleteNode(root.left, root.val)
        return root








        if not root: return None

        if root.val == key:
            if not root.left and not root.right: return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            right_child = root.right
            while right_child.left: 
                right_child = right_child.left
            
            root.val, right_child.val = right_child.val, root.val
            root.right = self.deleteNode(root.right, key)

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        
        return root