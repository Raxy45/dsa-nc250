# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = -1
        def dfs(root):
            nonlocal ans

            if not root: return 0
            # traverse to left, till the end
            left = dfs(root.left)

            # traverse to right, till the end
            right = dfs(root.right)
            
            # this will calculate the length:
            # 1. when we are at junction:
                #         1
                #        / \
                #       2   3
                # then at we will take sum of length of 2 and 3

            # 2. for non junction, either left or right will be zero. so no harm in adding left and right
            ans = max(ans, left+right)

            return 1 + max(left, right)
        dfs(root)
        return ans
        