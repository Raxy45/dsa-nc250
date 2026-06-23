# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSimilar(self, node1, node2):
        if not node1 and not node2: return True
        if not node1 or not node2 or node1.val!=node2.val: 
            return False
        return self.isSimilar(node1.left, node2.left) and self.isSimilar(node1.right, node2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        q1 = deque([root])
        while q1:
            for i in range(len(q1)):
                print(q1)
                popped = q1.popleft()
                if not popped: continue
                if popped.val == subRoot.val:
                    print('is it?')
                    if self.isSimilar(popped, subRoot):
                        return True
                q1.append(popped.left)
                q1.append(popped.right)
        return False
                    