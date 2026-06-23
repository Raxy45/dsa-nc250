class TrieNode:
    def __init__(self, char=None, eow=False):
        self.char = char
        self.children = {}
        self.eow = eow

class Solution:

    def insert(self, word, root):
        curr = root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.eow = True
    
    def starts_with(self, prefix, root):
        curr = root
        for char in prefix:
            if char not in curr.children: return False
            curr = curr.children[char]
        return True
        
    def search(self, prefix, root):
        curr = root
        for char in prefix:
            if char not in curr.children: return False
            curr = curr.children[char]
        return curr.eow

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        def search_02(idx, curr):
            print('searching from', idx, curr)
            i = idx
            subs = ""
            root = curr
            waste_chars = len(s)-idx
            while i<len(s):
                subs += s[i]
                if s[i] not in curr.children: break
                curr = curr.children[s[i]]
                if self.starts_with(subs, root) and self.search(subs, root):
                    print('found word in dict', subs)
                    waste_chars = search_02(i+1, curr)
                i += 1

            print(waste_chars, len(s)-idx)
            return min(waste_chars, len(s)-idx)
        self.root = TrieNode()

        for word in dictionary:
            self.insert(word, self.root)
        
        i, subs = 0, ""
        curr = self.root
        return search_02(0, curr)

        
                
                        