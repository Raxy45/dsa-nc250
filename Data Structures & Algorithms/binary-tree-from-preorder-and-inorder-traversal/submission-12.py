# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_index = 0
        self.inorder_map = {val: idx for idx, val in enumerate(inorder)}
        print(f'{self.inorder_map = }')
        def construct(left, right):
            if self.pre_index > len(inorder) or left>right: return None
            if left==right:
                print('left==right, forming node for',inorder[left])
                self.pre_index += 1
                return TreeNode(inorder[left])
            
            print('left, right', left, right)
            print(f'{self.pre_index = }')
            current_root_val = preorder[self.pre_index]
            self.pre_index += 1
            current_root_index_in_inorder = self.inorder_map[current_root_val]
            print(f'{current_root_val =}')
            print(f'{current_root_index_in_inorder = }')
            new_node = TreeNode(current_root_val)
            new_node.left = construct(left, current_root_index_in_inorder-1)
            new_node.right = construct(current_root_index_in_inorder + 1, right)
            return new_node
        return construct(0, len(preorder)-1)

