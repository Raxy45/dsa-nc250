class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = [0] * 26
        max_window, max_f = 0, 0
        l = 0
        for r in range(len(s)):
            freq_map[ord(s[r])-ord('A')] += 1

            max_f = max(max_f, freq_map[ord(s[r])-ord('A')])
            window_length = r - l +1
            if (window_length - max_f) > k:
                freq_map[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            max_window = max(max_window, r-l+1)
        return max_window