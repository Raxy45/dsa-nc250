class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        for word in strs:
            current_char_map = {}
            for i in range(len(word)):
                current_char_map[word[i]] = current_char_map.get(word[i], 0) + 1
            current_char_map = dict(sorted(current_char_map.items()))
            word_map[word] = current_char_map
        print(word_map)
        # final_list = [/÷]
        # for word_mapped_to_dict in word_map:

        from collections import OrderedDict
        new_word_map = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in new_word_map:
                new_word_map[sorted_word].append(word)
            else:
                new_word_map[sorted_word] = [word]
            # new_word_map[sorted_word] = new_word_map.get(sorted_word, []).append(sorted_word)
        
        ans = []
        for i in new_word_map:
            ans.append(new_word_map[i]) 
        return ans