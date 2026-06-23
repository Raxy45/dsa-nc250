# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q, s = deque([root]), []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    s.append(str(node.val))
                    s.append('#')
                    q.append(node.left)
                    q.append(node.right)
                else:
                    s.append('N#')
            s.append('*')
        print(s)
        return "".join(s)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        levels = data.split('*')
        print(levels)
        root_val = levels[0].split('#')[0]
        root = TreeNode(root_val)
        q = deque([root])
        while q:
            node = q.popleft()
            for level in levels[1:]:
                nums = level.split('#')[:-1]
                for n in nums:
                    if n == 'N':
                        node.left = None
                        
        return None