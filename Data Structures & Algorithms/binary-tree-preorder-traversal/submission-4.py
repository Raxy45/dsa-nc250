# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversalstk(self,root):
        ans = []
        stk = []
        curr = root
        while curr or stk:
            while curr:
                stk.append(curr)
                ans.append(curr.val)
                curr = curr.left
            popped_node = stk.pop()
            curr = popped_node.right
        
        return ans
    def preorderTraversalRec(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traversal(node):
            if not node:
                return
            
            ans.append(node.val)
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        return ans
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        ans = []
        while curr:
            if curr.left==None:
                ans.append(curr.val)
                # we again move to root of tree
                curr = curr.right
            else:
                left_child = curr.left
                while left_child.right and left_child.right != curr:
                    left_child = left_child.right
                
                if left_child.right==None:
                    left_child.right = curr
                    ans.append(curr.val) # when you are at root, and before moving to left of tree, you add this to ans
                    curr = curr.left
                else:
                    # when left_child.right points to curr, meaning we have already visited the left subtree of curr 
                    curr = curr.right

                    left_child.right = None # removing the link, which we had created
        return ans