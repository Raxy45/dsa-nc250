class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1p, w2p = 0,0
        np = 0
        ans_w = [0]*(len(word1)+len(word2))
        while w1p<len(word1) and w2p<len(word2):
            print(np, np%2)
            if np%2==0:
                ans_w[np] = word1[w1p]
                w1p += 1
            else:
                ans_w[np] = word2[w2p]
                w2p += 1
            np += 1
        
        while w1p<len(word1):
            ans_w[np] = word1[w1p]
            w1p += 1
            np += 1

        while w2p<len(word2):
            ans_w[np] = word2[w2p]
            w2p += 1
            np += 1
        return ''.join(ans_w)