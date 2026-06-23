class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, subset = [], []
        num = 1
        def solve(num):
            # print(subset, num)
            if len(subset) == k:
                ans.append(subset.copy())
                return
            
            if num>n: return
            subset.append(num)
            solve(num+1)

            subset.pop()
            solve(num+1)
        
        solve(num)
        return ans