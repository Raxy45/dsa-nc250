class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        pars = []
        def solve(current_str, openN, closeN):
            print(current_str, openN, closeN)
            if len(current_str)==2*n:
                res.append("".join(current_str))
                return

            if openN<n:
                current_str.append('(')
                print('in openN: ', current_str, openN+1, closeN)
                solve(current_str, openN+1, closeN)
                current_str.pop()

            if closeN<openN:
                current_str.append(')')
                solve(current_str, openN, closeN+1)
                current_str.pop()
        
        solve(pars, 0,0)
        return res