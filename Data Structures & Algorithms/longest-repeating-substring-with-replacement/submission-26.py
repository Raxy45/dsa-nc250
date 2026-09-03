class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0]*26
        l = 0
        max_f = 0
        max_window = 0
        for r in range(len(s)):
            freq[ord(s[r])-ord('A')] += 1
            max_f = max(max_f, freq[ord(s[r])-ord('A')])
            window_length = r - l + 1
            # if (Total Chars - max_frequency of char) > k -> remove one char from the left
            while ((r - l + 1)-max_f) > k:
                freq[ord(s[l])-ord('A')] -= 1
                l += 1
            window_length = r - l +1
            max_window=max(max_window, window_length)
            # print(l, r, freq)

        return max_window
        