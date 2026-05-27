# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        if not root: return 0
        q = deque([(root, 1)])
        mx_ht = 0
        while q:
            for _ in range(len(q)):
                node, height = q.pop()
                mx_ht = max(height, mx_ht)
                if node.left:
                    q.append((node.left, height+1))
                if node.right:
                    q.append((node.right, height+1))
        return mx_ht
    def maxDepthRec(self, root):
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
    def maxDepthStk(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        max_d, stk = 0, [(root, 1)]

        while stk:
            node, height = stk.pop()
            max_d = max(max_d, height)
            if node.left:
                stk.append((node.left, height+1))
            if node.right:
                stk.append((node.right, height+1))
        return max_d
    
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
    def maxDepthME(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        max_d = 1
        def dfs(node, height):
            nonlocal max_d
            if not node: return
            max_d = max(max_d, height)
            dfs(node.left, height+1)
            dfs(node.right, height+1)
        
        dfs(root, 1)
        return max_d