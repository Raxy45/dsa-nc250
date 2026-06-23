class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_word_map = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in new_word_map:
                new_word_map[sorted_word].append(word)
            else:
                new_word_map[sorted_word] = [word]
        
        ans = []
        for i in new_word_map:
            ans.append(new_word_map[i]) 
        return ans