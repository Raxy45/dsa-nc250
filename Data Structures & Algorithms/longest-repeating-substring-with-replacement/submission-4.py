class Solution:
    def get_max_count(c_map):
        sorted_items = sorted(c_map.items(), key=lambda item: item[1], reverse=True)
        # Convert the sorted list of tuples back into a dictionary (optional)
        sorted_dict = dict(sorted_items)

        print(sorted_dict)
        max_char, max_count = next(iter( sorted_dict.items() ))
        return max_count
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0]*26
        l = 0
        max_f = 0
        max_window = 0
        for r in range(len(s)):
            freq[ord(s[r])-ord('A')] += 1
            max_f = max(max_f, freq[ord(s[r])-ord('A')])
            window_length = r - l + 1
            if window_length-max_f > k:
                freq[ord(s[l])-ord('A')] -= 1
                l += 1
            window_length = r - l +1
            max_window=max(max_window, window_length)

        return max_window
            



        longest_len = 0

        if len(s) == 1:
            return 1



        l, r = 0, 1
        char_map = {s[0:1]:1}
        longest = 0
        while r < len(s):
            current_char = s[r:r+1]
            window_length = r-l+1
            max_char = char_map.sort()
        for i in range(0, len(s)):
            current_replace = k
            current_outer_char = s[i:i+1]
            j = i
            while j >0 and (current_replace) > 0:
                j -= 1
            current_longest = 0
            print('current char: ', s[i:i+1])
            while j < len(s):
                char = s[j:j+1]
                print('current j: ', char)
                print('current longest: ', current_longest)
                if char == current_outer_char:
                    j += 1
                    current_longest += 1
                    print('A match. c_long: ', current_longest)
                else:
                    print('not a match')
                    if current_replace > 0:
                        print('decreasing k by 1')
                        current_replace -= 1
                        j += 1
                        current_longest += 1
                    else:
                        print('cant decrease')
                        break
            longest_len = max(longest_len, current_longest)
        return longest_len
