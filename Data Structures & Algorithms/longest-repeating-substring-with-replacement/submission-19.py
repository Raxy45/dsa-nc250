class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        c = defaultdict(int)
        max_c = float('-inf')
        max_len = 0
        while r<len(s):
            char = s[r]
            c[char] += 1
            max_c = max(max_c, c[char])
            current_len = (r-l+1)
            if (current_len-max_c)>k:
                char_to_be_removed = s[l]
                removed_char_freq = c[char_to_be_removed]
                c[char_to_be_removed] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
            r += 1
        return max_len

