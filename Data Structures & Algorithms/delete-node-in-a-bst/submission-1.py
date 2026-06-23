# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # we are at node, which you want to delete 
            if not root.right:
                # example deleting 5 from
            #         2         2 
            #        / \       / \   
            #       1.  5  -> 1.  4
            #          /
            #         4
                return root.left
            if not root.left:
                # example deleting 5 from
            #         2         2 
            #        / \       / \   
            #       1   5  -> 1   6
            #            \ 
            #             6 
                return root.right

            # finding the left most child of right subtree
            curr = root.right
            while curr and curr.left:
                curr = curr.left
            
            root.val = curr.val
            # since you duplicated value from the right subtree, you will have to delete
            # the node which got copied into root from right subtree
            root.right = self.deleteNode(root.right, root.val)
        return root