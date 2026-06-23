# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        q = deque([root])
        while q:
            curr = []
            for i in range(len(q)):
                popped = q.popleft()
                if popped:
                    curr.append(popped.val)
                    q.append(popped.left)
                    q.append(popped.right)
            if curr:
                ans.append(curr[-1])
        return ans