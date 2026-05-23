class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        i = 0
        curr = ""
        while i < len(path):
            while i<len(path) and path[i] == '/':
                i += 1
            
            curr = ""
            while i<len(path) and path[i]!= '/':
                curr += path[i]
                i += 1
            
            if curr == '.':
                continue
            
            if curr == '..':
                if len(stk) > 0:
                    stk.pop()
            elif len(curr) > 0:
                stk.append(curr)
        # print(stk)
        return '/' + "/".join(stk)