class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        curr_path = ''
        for curr_char in path+'/':
            print(stk, curr_path, curr_char)
            if curr_char == '/':
                if curr_path == '..':
                    if stk: stk.pop()
                elif curr_path == '' or curr_path == '.' or curr_path == '/':
                    pass
                else:
                    stk.append(curr_path)
                curr_path = ''
            else:
                curr_path += curr_char
        return '/' + "/".join(stk)