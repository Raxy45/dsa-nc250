# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root):
        if not root: return None
        curr, stk = root, []
        while curr or stk:
            while curr:
                stk.append((curr, False))
                curr = curr.left
            
            # print('curr', curr)
            # print(stk)
            # print('****')
            node, visited = stk.pop()
            if not visited:
                stk.append((node, True))
                curr = node.right
            else:
                node.left, node.right = node.right, node.left
        return root
        # print(
        #     'nooo'
        # )