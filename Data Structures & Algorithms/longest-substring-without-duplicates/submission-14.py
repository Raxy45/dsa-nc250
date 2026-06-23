class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 1
        if len(s)==0:
            return 0
        i,j=0,0
        char_map[s[i]] = 0
        for j in range(1, len(s)):
            while s[j] in char_map:
                char_map.pop(s[i])
                i+=1
            char_map[s[j]]=1
            max_length = max(max_length, j-i+1)
        return max_length
        uniq_set = set([])
        l = r = 0
        max_count = 0
        for r in range(0, len(s)):
            current_char = s[r:r+1]
            while l <=r and current_char in uniq_set:
                uniq_set.remove(s[l])
                l += 1
            uniq_set.add(current_char)
            max_count = max(max_count, len(uniq_set))
        return max_count 
        uniq_set = set([])
        l = r = 0
        max_count = 0
        for i in range(0, len(s)):
            current_char = s[i:i+1]
            if current_char not in uniq_set:
                uniq_set.add(current_char)
                r += 1
            else:
                while l <=r and current_char in uniq_set:
                    uniq_set.remove(s[l])
                    l += 1
                uniq_set.add(current_char)
                r += 1
            max_count = max(max_count, len(uniq_set))
        return max_count 
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