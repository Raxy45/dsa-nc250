class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for r in operations:
            if r == '+':
                stk.append(stk[-1] + stk[-2])
            elif r == 'C':
                stk.pop()
            elif r == 'D':
                stk.append(stk[-1] * 2)
            else:
                stk.append(int(r))
        print(stk)
        return sum(stk)