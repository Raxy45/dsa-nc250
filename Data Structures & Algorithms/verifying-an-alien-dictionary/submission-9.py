class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx_mp = {}
        c = 0
        for s in order:
            idx_mp[s] = c
            c += 1
        print(idx_mp)

        indx = 0
        # return True
        while True:
            sorted_count = 0
            idx_exists = False
            for i in range(0, len(words)-1):
                w1, w2 = words[i], words[i+1]
                # print(indx, w1, w2)
                if indx >= len(w1) and indx>= len(w2):
                    continue

                idx_exists = True
                if indx>=len(w2):
                    # neetcode, neet
                    return False
                
                if indx>=len(w1):
                    # neet, neetcode
                    continue

                c1, c2 = w1[indx], w2[indx]
                if idx_mp[c1] > idx_mp[c2]:
                    return False
                if idx_mp[c1] == idx_mp[c2]:
                    continue

                if idx_mp[c1] < idx_mp[c2]:
                    sorted_count += 1
                
            if sorted_count==len(words)-1 or not idx_exists: return True

            indx += 1
            

             