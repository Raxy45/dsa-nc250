class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1: return 1
        j, max_l, window = 0, 0, set()
        for i in range(len(s)):
            print(max_l)
            while j<=i and s[i] in window:
                print('removing till', s[i], 'not in window')
                window.remove(s[j])
                max_l = max(max_l, i - j)
                j += 1
                print('updated window and j', window, j)

            # if s[i] not in window:
                # print('Adding', s[i], 'in window')
            window.add(s[i])
                # continue
            print('*'*4)
        return max(max_l, i-j)