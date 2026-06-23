class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        curr_sentence = []
        index_sentences = defaultdict(list)
        wordDict_d = {key: True for key in wordDict}
        print(wordDict_d)
        def solve(i):
            if i==len(s):
                ans.append(" ".join(curr_sentence))
                return

            word = "" 
            for k in range(i, len(s)):
                word += s[k]
                if wordDict_d.get(word):

                    index_sentences[i].append(word)
                    curr_sentence.append(word)

                    if (k+1) in index_sentences:
                        # already computed all the words starting from k+1 index
                        ans.append(" ".join((curr_sentence + index_sentences[i])))
                        index_sentences[i].append(index_sentences[i])
                        continue
                    solve(k+1)
                    curr_sentence.pop()
        solve(0)
        return ans        
        