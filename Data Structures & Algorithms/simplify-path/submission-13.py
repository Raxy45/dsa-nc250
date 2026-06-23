class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        curr_path = ""
        path += '/'
        for i in range(len(path)):
            char = path[i]
            if char != '/':
                curr_path += char
                continue

            if char == '/':
                if curr_path == '':
                    continue
                if curr_path == '.':
                    curr_path = ''
                    continue
                
                if curr_path == '..':
                    if stk: stk.pop()
                    curr_path = ''
                    continue
                
                stk.append(curr_path)
                curr_path = ''
                
        return '/'+"/".join(stk)
                 