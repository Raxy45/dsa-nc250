class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)

        stk = []
        for i in range(len(temperatures)):
            curr_t = temperatures[i]
            while stk and temperatures[stk[-1]]<curr_t:
                popped_idx = stk.pop()
                ans[popped_idx] = i - popped_idx
            stk.append(i)
        
        return ans