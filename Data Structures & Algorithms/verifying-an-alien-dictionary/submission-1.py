class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        indx_mp = {char: indx for indx, char in enumerate(order)}
        
        if len(words) == 1: return True


        def solve(w1, w2):
            max_w = max(len(w1), len(w2))
            print('current w1, w2', w1, w2)

            for i in range(max_w):
                print(i)
                indx_w1 = indx_mp[w1[i]] if i<len(w1) else float('inf')
                indx_w2 = indx_mp[w2[i]] if i<len(w2) else 0
                print(indx_w1, indx_w2)
                if indx_w1 == indx_w2: 
                    continue
                if indx_w1<indx_w2:
                    return True
                return False
            

        for i in range(1, len(words)):
            word_1, word_2 = words[i-1], words[i]
            if not solve(word_1, word_2):
                print('false for solve')
                return False
        return True