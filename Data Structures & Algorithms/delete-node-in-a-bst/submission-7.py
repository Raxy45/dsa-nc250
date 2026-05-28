# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        if root.val == key:
            if root.left and not root.right:
                tbd = root.left
                del root
                return tbd
            elif root.right and not root.left:
                tbd = root.right
                del root
                return tbd
            elif root.right and root.left:
                # both the children exists
                print('root has 2 children', root.val)
                right_child = root.right
                if right_child:
                    while right_child.left:
                        right_child = right_child.left
                    print('setting root to', root.val, right_child.val)
                    root.val = right_child.val
                    root.right = self.deleteNode(root.right, right_child.val)
                else:
                    print('setting root to right',root.val, right_child.val)
                    root.val = right_child.val
                    root.right=None
            else:
                # leaf node
                return None
        elif val > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # val < root.val
            root.left = self.deleteNode(root.left, key)
        return root
        
