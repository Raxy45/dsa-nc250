class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]* len(temperatures)
        mtc_stk = []
        for i in range(0, len(temperatures)):
            while len(mtc_stk) > 0 and temperatures[i] > temperatures[mtc_stk[-1]]:
                idx = mtc_stk.pop()
                result[idx] = i-idx
            mtc_stk.append(i)
        return result