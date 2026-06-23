# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        curr = root

        while curr:
            if not curr.right:
                ans.append(curr.val)
                curr = curr.left
            else:
                right_child = curr.right
                while right_child.left and right_child.left!=curr:
                    right_child = right_child.left
                
                if not right_child.left:
                    right_child.left = curr
                    ans.append(curr.val)
                    curr = curr.right
                else:
                    right_child.left= None
                    curr = curr.left
        ans.reverse()
        return ans

        while cur:
            if not cur.right:
                res.append(cur.val)
                cur = cur.left
            else:
                prev = cur.right
                while prev.left and prev.left != cur:
                    prev = prev.left

                if not prev.left:
                    res.append(cur.val)
                    prev.left = cur
                    cur = cur.right
                else:
                    prev.left = None
                    cur = cur.left

        res.reverse()
        return res

    def postorderTraversalStk(self, root: Optional[TreeNode]) -> List[int]:
        stk, ans = [], []
        curr = root
        while curr or stk:
            while curr:
                stk.append((curr, False))
                curr = curr.left
            
            node, visited = stk.pop()
            if visited:
                ans.append(node.val)
                continue
            stk.append((node, True))
            curr = node.right
        return ans