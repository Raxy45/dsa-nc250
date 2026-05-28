# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        print('Deleting', root, key)
        if not root: return None
        print(root.val)
        if key > root.val:
            print('<', val, root.val, val>root.val)
            root.right = self.deleteNode(root.right, key)
            return root
        elif key < root.val:
            print('>', val, root.val, val<root.val)
            root.left = self.deleteNode(root.left, key)
            return root
        
        # root.val == key
        if root.left and not root.right:
            print('first')
            return root.left
        elif root.right and not root.left:
            print('seoncd')
            return root.right
        elif not root.left and not root.right:
            # leaf node
            print('returning None, as leaf node')
            return None
        
        print('has both the children')
        right_child = root.right
        while right_child.left:
            right_child = right_child.left
        
        print('end of root', root.val, right_child.val)
        root.val = right_child.val
        print('updated val', root.val)
        root.right = self.deleteNode(root.right, root.val)
        print('here for',root.val)
        return root