class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = Counter(t)

        needed = len(t_map)
        formed = 0
        slow, fast = 0, 0
        s_map = {}
        ans = s+t
        print(t_map)
        for i in range(len(s)):
            curr_char = s[i]
            s_map[curr_char] = s_map.get(curr_char, 0) + 1

            if s_map[curr_char] == t_map.get(curr_char, 0):
                formed += 1
            
            print(s_map, formed)
            # print(slow, i, formed)
            while formed == needed:
                curr_ans = s[slow:i+1]
                if len(curr_ans) <= len(ans):
                    ans = curr_ans
                char_at_slow = s[slow]
                s_map[char_at_slow] -= 1
                slow += 1

                if s_map[char_at_slow] < t_map[char_at_slow]:
                    formed -= 1
            print('after', s_map, formed)
            # print(slow, i, formed)
            print('*'*6)
        if ans == s + t: return ""
        return ans