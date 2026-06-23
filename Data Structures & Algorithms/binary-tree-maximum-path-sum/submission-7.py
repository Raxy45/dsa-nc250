# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def getSum(root):
            nonlocal ans
            if not root: return 0

            left_child_max_sum = getSum(root.left)
            right_child_max_sum = getSum(root.right)

            left_child_max_sum = max(0, left_child_max_sum)
            right_child_max_sum = max(0, right_child_max_sum)

            ans = max(ans, root.val+left_child_max_sum+right_child_max_sum)

            return root.val + max(left_child_max_sum, right_child_max_sum)
        
        getSum(root)
        return ans