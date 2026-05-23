class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stk = []
        ans = [0] * len(t)
        for i in range(len(t)):
            print(stk, ans, i, 'b4')
            while stk and t[i] > t[stk[-1]]:
                ans[stk[-1]] = i - stk[-1]
                stk.pop()
            stk.append(i)
            print(stk, ans, i, 'after')
            print('**')
        return ans