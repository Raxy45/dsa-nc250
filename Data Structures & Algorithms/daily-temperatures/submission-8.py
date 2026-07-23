class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                popped_idx = stk.pop()
                ans[popped_idx] = i - popped_idx
            
            stk.append(i)
        return ans