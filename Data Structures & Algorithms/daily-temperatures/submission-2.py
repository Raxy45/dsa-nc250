class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]* len(temperatures)
        stk = []
        for i in range(len(temperatures)-1, -1, -1):
            t = temperatures[i]
            while len(stk) > 0 and t>=temperatures[stk[-1]]:
                stk.pop()
            if len(stk)==0:
                result[i] = 0
            else:
                result[i] = stk[-1]-i
            stk.append(i)
           
        return result
        mtc_stk = []
        for i in range(0, len(temperatures)):
            while len(mtc_stk) > 0 and temperatures[i] > temperatures[mtc_stk[-1]]:
                idx = mtc_stk.pop()
                result[idx] = i-idx
            mtc_stk.append(i)
        return result