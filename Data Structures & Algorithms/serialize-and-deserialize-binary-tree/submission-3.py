# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return 'N'
        arr, q = [], deque([root])
        while q:
            node = q.popleft()
            if not node:
                arr.append('N')
            else:
                arr.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ','.join(arr)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == 'N': return None
        vals = data.split(',')
        print(vals)
        root = TreeNode(int(vals[0]))
        q = deque([root])
        node_val_index = 1
        while q:
            node = q.popleft()
            
            lhs_node = vals[node_val_index]
            if lhs_node == 'N':
                node.left = None
            else:
                node.left = TreeNode(int(vals[node_val_index]))
                q.append(node.left)

            node_val_index += 1
            
            rhs_node = vals[node_val_index]
            if rhs_node == 'N':
                node.right = None
            else:
                node.right = TreeNode(int(vals[node_val_index]))
                q.append(node.right)
            node_val_index += 1
        return root
