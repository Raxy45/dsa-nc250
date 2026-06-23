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

        ans, temp = [], []
        def solve(idx, c_idx):
            print(temp, idx, c_idx)
            if idx == len(digits):
                ans.append("".join(temp.copy()))
                return
            
            digit = digits[idx]
            chars = mappings[digit]
            for j in range(0, len(chars)):
                temp.append(chars[j])
                solve(idx+1, j+1)
                temp.pop()
                    
        if len(digits) == 0: return []
        solve(0, 0)
        return ans