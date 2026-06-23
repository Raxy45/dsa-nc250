class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if '0000' in deadends:
            return -1
        counter = 0
        q = deque([('0000', 0)])

        def get_children(parent):
            children = []
            for i in range(4):
                val = int(parent[i])
                incre = (val+1)%10
                decre = (val - 1 + 10)%10

                incre_val = parent[:i] + str(incre) + parent[i+1:]
                decre_val = parent[:i] + str(decre) + parent[i+1:]

                children.append(incre_val)
                children.append(decre_val)
            return children

        while q:
            current_parent, turns = q.popleft()
            if current_parent == target:
                return turns

            children = get_children(current_parent)
            for child in children:
                if child not in visited:
                    q.append((child, turns + 1))
                    visited.add(child)
                    
            
            counter += 1
        
        return -1