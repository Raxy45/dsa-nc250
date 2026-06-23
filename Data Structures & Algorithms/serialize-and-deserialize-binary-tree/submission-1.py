# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        node_val = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                node_val.append('N')
            else:
                node_val.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        print(','.join(node_val))
        return ','.join(node_val)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data[0] == 'N': return None

        vals = data.split(',')
        print(vals)

        root = TreeNode(int(vals[0]))
        q = deque([root])
        index = 1
        while q:
            node = q.popleft()
            if vals[index]!='N':
                node.left = TreeNode(int(vals[index]))
                q.append(node.left)
            
            index += 1
            if vals[index] != 'N':
                node.right = TreeNode(int(vals[index]))
                q.append(node.right)
            index+=1
        return root
        