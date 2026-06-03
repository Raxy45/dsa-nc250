class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        mappings = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }


        ans, subset = [], []
        def solve(idx):
            if idx==len(digits):
                ans.append("".join(subset.copy()))
                return 
            
            current_chars = mappings[digits[idx]]
            for char in current_chars:
                subset.append(char)
                solve(idx+1)
                subset.pop()
            
        solve(0)
        print(ans)
        return ans