class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans, stk = [0] * len(temperatures), []
        for i in range(len(temperatures)):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                popped_index = stk.pop()
                ans[popped_index] = i - popped_index
            stk.append(i)
        return ans