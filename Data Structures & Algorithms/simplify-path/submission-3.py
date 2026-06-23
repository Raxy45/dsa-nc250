class Solution:
    def simplifyPath(self, path) -> str:
        stk = []
        curr = ""
        for char in path+'/':
            print('curr ', curr)
            print('char ', char)
            print(stk)
            print('*'*30)
            if char == '/':
                if curr == '..':
                    if len(stk) > 0:
                       stk.pop()
                elif curr == '' or curr == '.':
                    continue
                else:
                    stk.append(curr)
                curr = ''
            else:
                curr += char
            
        return '/'+"/".join(stk)

    def simplifyPathEasy(self, path: str) -> str:
        updated_path = path[1:].split('/')
        stk = []
        print(updated_path)
        for c_path in updated_path:
            print('current path ', c_path)
            if len(c_path) == 0 or c_path == '.':
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