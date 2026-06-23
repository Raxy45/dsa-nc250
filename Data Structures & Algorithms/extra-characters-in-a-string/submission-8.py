class TrieNode:
    def __init__(self, char=None, eow=False):
        self.char = char
        self.eow = eow
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.parent = TrieNode()

    def construct(self, dictionary):
        for word in dictionary:
            curr = self.parent
            i = 0
            while i < len(word):
                curr_char = word[i]
                if curr_char not in curr.children:
                    new_node = TrieNode(curr_char)
                    curr.children[curr_char] = new_node
                curr = curr.children[curr_char]
                i += 1
            curr.eow = True
    
class Solution:
    def minExtraChar(self, word: str, dictionary: List[str]) -> int:
        trie = Trie()
        trie.construct(dictionary)
        ans = float('inf')
        def dfs(idx, curr):
            nonlocal ans
            if idx==len(word) and curr.eow: return 0

            for i in range(idx, len(word)):
                if not curr: break
                curr_char = word[i]
                if curr_char not in curr.children:
                    ans = min(ans, len(word) - idx)
                    return ans
                curr = curr.children[curr_char]
                if curr.eow:
                    # you can split or you continue
                    ans = min(ans, dfs(i+1, trie.parent))
            
            ans = min(ans, length(word)-i)
            return ans
        return dfs(0, trie.parent)
        