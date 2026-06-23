# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        stk = [root]
        ans = []
        curr = root
        while stk:
            while curr and curr.left:
                stk.append(curr.left)
                curr = curr.left
            popped_node = stk.pop()
            ans.append(popped_node.val)
            if popped_node.right:
                curr = popped_node.right
                stk.append(popped_node.right)
        return ans
    def inorderTraversalRecursion(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traverse(node):
            if not node:
                return

            traverse(node.left)
            ans.append(node.val)
            traverse(node.right)

        traverse(root)
        return ans