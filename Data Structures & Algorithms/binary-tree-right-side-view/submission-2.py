# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque([root])
        ans = []
        while q:
            for _ in range(len(q)-1):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            node = q.popleft()
            print('popped out node', node)
            if node:
                print(node.val)
                ans.append(node.val)
                print(ans)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            print(q)
            print('**')
        return ans
        