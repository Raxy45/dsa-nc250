# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val

        def dfs(root):
            nonlocal ans
            if not root: return 0

            left_subtree_sum = dfs(root.left)

            right_subtree_sum = dfs(root.right)
            ans = max(ans, left_subtree_sum+right_subtree_sum+root.val, root.val)

            return max(left_subtree_sum+root.val, right_subtree_sum+root.val, root.val)
        dfs(root)
        return ans

    def maxPathSumMe(self, root: Optional[TreeNode]) -> int:
        ans = root.val

        def dfs(root):
            nonlocal ans
            if not root: return [0,0]

            [a,b] = dfs(root.left)
            max_sum_with_left_subtree = max(a + root.val, b + root.val, root.val)

            [c,d] = dfs(root.right)
            max_sum_with_right_subtree = max(c+root.val, d + root.val, root.val)

            # print(a,b,c,d)
            # print(root.val)
            # print(max_sum_with_left_subtree)
            # print(max_sum_with_right_subtree)
            # print(max_sum_with_left_subtree + max_sum_with_right_subtree - root.val)
            # print('*'*20)

            ans = max(max_sum_with_left_subtree, \
                      max_sum_with_right_subtree, \
                      max_sum_with_left_subtree + max_sum_with_right_subtree - root.val, ans)

            return [max_sum_with_left_subtree, max_sum_with_right_subtree]
        dfs(root)
        return ans