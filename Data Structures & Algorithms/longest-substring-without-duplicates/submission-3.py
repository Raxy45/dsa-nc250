class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans_arr = []
        max_count = 0
        if len(s) == 1:
            return 1
        for i in range(0, len(s)):
            current_char = s[i:i+1]
            if current_char not in ans_arr:
                ans_arr.append(current_char)
            else:
                k = 0
                while k<len(ans_arr) and ans_arr[k] != current_char:
                    k += 1
                if k == len(ans_arr)-1:
                    ans_arr = []
                else:
                    ans_arr = ans_arr[k+1:]
                ans_arr.append(current_char) 
            max_count = max(max_count, len(ans_arr))
        return max_count 
        
        str_set = set([])
        max_count = 0
        current_count = 0
        if len(s) == 1:
            return 1
        for i in range(0, len(s)):
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