class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        for i in range(len(temperatures)):
            current_diff = 0
            for j in range(i, len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    current_diff = j-i
                    break
            ans.append(current_diff)
        return ans