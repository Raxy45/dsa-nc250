class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for w in dictionary:
            trie.addWord(w)
        dp = {len(s):0}
        def dfs(idx):
            if idx in dp: return dp[idx]
            res = 1 + dfs(idx + 1)

            curr = trie.root
            for j in range(idx, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.isWord:
                    res = min(res, dfs(j+1))
            dp[idx] = res
            return res
        return dfs(0)
    def minExtraChar1DP(self, s: str, dictionary: List[str]) -> int:
        dp = {len(s):0}
        def dfs(idx):
            if idx in dp: return dp[idx]
            res = 1 + dfs(idx + 1)

            for j in range(idx, len(s)):
                if s[idx:j+1] in dictionary:
                    res = min(res, dfs(j+1))
            dp[idx] = res
            return res
        return dfs(0)