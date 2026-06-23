class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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

        ans, curr = [], []
        def solve(idx, curr):
            if idx == len(digits):
                ans.append("".join(curr))
                return
            
            current_chars = mappings[digits[idx]]
            for char in current_chars:
                curr.append(char)
                solve(idx+1, curr)
                curr.pop()
        
        if len(digits) == 0: return []
        solve(0, curr)
        return ans
