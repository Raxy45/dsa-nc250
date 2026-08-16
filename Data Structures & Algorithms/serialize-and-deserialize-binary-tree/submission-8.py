# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = ""
        curr = root
        if not root:
            return ""
        q = deque([root])
        while q:
            curr = q.popleft()
            if not curr:
                s  = s + 'N#'
                continue
            s = s + str(curr.val) + '#' 
            q.append(curr.left)
            q.append(curr.right)
        print(s, type(s))
        return s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        data = deque(data.split('#')[:-1])
        head = parent_node = TreeNode(int(data.popleft()))
        pq = deque([parent_node])
        while pq:
            parent = pq.popleft()
            lhs = data.popleft()
            if lhs!='N':
                lhs = TreeNode(int(lhs))
                parent.left = lhs
                pq.append(lhs)

            rhs = data.popleft()
            if rhs!="N":
                rhs = TreeNode(int(rhs))
                parent.right = rhs
                pq.append(rhs)
        return head

        