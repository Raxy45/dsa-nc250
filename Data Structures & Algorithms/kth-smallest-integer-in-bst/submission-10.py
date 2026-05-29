# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = []
        count = 1
        while stk or root:
            while root:
                # print('adding',root.val)
                stk.append(root)
                root = root.left
            
            node = stk.pop()
            
            if node:
                # print('popped node', node.val, node.right)
                if count==k:
                    return node.val
                count += 1
                root = node.right
        # print(preorder)
        # return preorder[k-1]
