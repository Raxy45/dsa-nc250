# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        ans = []
        stk = []
        curr = root
        while curr or stk:
            while curr:
                stk.append((curr, False))
                curr = curr.left
            
            (node, visited) =  stk[-1]
            if node.right is not None and visited is False:
                stk[-1] = (node, True)
                curr = node.right
            else:
                ans.append(node.val)
                stk.pop()
        return ans

    def postorderTraversalStk(self, root: Optional[TreeNode]) -> List[int]:
        ans: List[int] = []
        stack: List[tuple[TreeNode, bool]] = []
        curr = root

        while curr or stack:
            while curr:
                stack.append((curr, False))
                curr = curr.left

            node, visited = stack[-1]
            if node.right==None or visited:
                ans.append(stack.pop()[0].val)
            else:
                # mark as visited and process right subtree
                stack[-1] = (node, True)
                curr = node.right

        return ans
    def postorderTraversalMe(self,root):
        ans = []
        stk = []
        curr = root
        c = 0
        while curr or stk:
            if c>10: break
            while curr:
                stk.append([curr, False])
                curr = curr.left

            if stk[-1][0].right and stk[-1][1] is False:
                stk[-1][1] = True
                curr = stk[-1][0].right
                # stk[-1].right = None
            else:
                ans.append(stk.pop()[0].val)
        return ans

    def postorderTraversalRecursion(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traversal(node):
            if not node: return

            traversal(node.left)
            traversal(node.right)
            ans.append(node.val)
        traversal(root)
        return ans