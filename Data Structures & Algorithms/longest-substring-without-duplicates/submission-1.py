class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_set = set([])
        max_count = 0
        current_count = 0
        if len(s) == 1:
            return 1
        for i in range(0, len(s)-1):
            current_char = s[i:i+1]
            print('char: ', current_char)
            print('set: ', str_set)
            print('max count: ', max_count)
            if current_char not in str_set:
                current_count += 1
                str_set.add(current_char)
            else:
                str_set = set([])
                str_set.add(current_char)
                current_count = 1
            max_count = max(max_count, current_count)
        return max_count