class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(start):
            # print(start)
            if len(comb) == k:
                res.append(comb.copy())
                return

            for i in range(start, n + 1):
                comb.append(i)
                # print('added i', i)
                backtrack(i + 1)
                comb.pop()

        backtrack(1)
        return res

    def combine2(self, n: int, k: int) -> List[List[int]]:
        ans, subset = [], []
        num = 1
        def solve(num):
            # print(subset, num)
            if len(subset) == k:
                ans.append(subset.copy())
                return
            
            if num>n: return

            # include num, form the subset for num included
            subset.append(num)
            solve(num+1)

            # exclude num, form the subset which does not include num
            subset.pop()
            solve(num+1)
        
        solve(num)
        return ans