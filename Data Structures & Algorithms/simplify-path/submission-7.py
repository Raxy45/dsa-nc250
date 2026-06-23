class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c

        return "/" + "/".join(stack)

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