class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        for c in path[1:]+"/":
            # print(cur)
            if c != '/':
                cur += c
            else:
                if cur == '/' or cur == '.':
                    pass
                elif cur == '..':
                    if len(stack)>0:
                        print('popping')
                        stack.pop()
                    cur = ''
                else:
                    if len(cur)>0:
                        print('appending', cur)
                        stack.append(cur)
                cur = ''
            print(stack)
        return "/"+"/".join(stack)

        for c in path + "/":
            if c == "/":
                if cur == "..":
                    # we wont reach here till we encounter a ...
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    # when we have a valid char formed like abc, ...
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