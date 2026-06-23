class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_len = 0

        if len(s) == 1:
            return 1
        for i in range(0, len(s)-1):
            current_replace = k
            j = i+1
            current_longest = 1
            print('current char: ', s[i:i+1])
            while j < len(s):
                char = s[j:j+1]
                print('current j: ', char)
                print('current longest: ', current_longest)
                if char == s[i:i+1]:
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
