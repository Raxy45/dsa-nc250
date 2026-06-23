class Solution:
    def simplifyPath(self, path: str) -> str:
        updated_path = path[1:].split('/')
        stk = []
        print(updated_path)
        for c_path in updated_path:
            print('current path ', c_path)
            if len(c_path) == 0:
                print(
                    'in empty'
                )
                continue
            elif c_path == '..':
                if len(stk) > 0:
                   stk.pop()
            else:
                print('appending to stk')
                stk.append(c_path)
        return '/'+ '/'.join(stk)