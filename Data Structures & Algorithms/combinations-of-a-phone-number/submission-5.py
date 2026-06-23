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
        def solve(d_idx, w):
            if d_idx == len(digits):
                ans.append(w)
                return
            
            char_map = mappings[digits[d_idx]]
            for c_idx in range(len(char_map)):
                w += char_map[c_idx]
                solve(d_idx+1, w)
                w = w[:len(w)-1]
        ans, w = [], ""
        solve(0, w)
        return ans