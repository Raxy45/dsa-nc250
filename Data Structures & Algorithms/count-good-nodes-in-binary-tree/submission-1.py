# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        ans = 0
        q = deque([(root, root.val)])
        while q:
            current, parent_max = q.popleft()
            if current.val >= parent_max:
                ans += 1
            current_max = max(current.val, parent_max)
            if current.left:
                q.append((current.left, current_max))
            if current.right:
                q.append((current.right, current_max))
        return ans