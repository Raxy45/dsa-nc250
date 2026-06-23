class TrieNode:
    def __init__(self):
        self.eof = False
        self.children = {}

class Tree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        
        curr.eof = True
    
    def search(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return curr.eof


    def starts_with(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return True


class Solution:
    def search_path(self, idx, curr, s):
        for i in range(idx, len(s)):
            if s[i] in curr.children:
                curr = curr.children[s[i]]
                continue
            self.unused += (i-idx)
            self.search_path(i + 1, self.tree.root, s)
            # s[i] does not exist in curr.children
                # we will have to begin searching from start of root

        
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        self.tree = Tree()
        self.unused = 0
        for word in dictionary:
            self.tree.insert(word)

        self.search_path(0, self.tree.root, s)
        return self.unused
        # word = ""
        # unused = 0
        # for i in range()
        # for char in s:
        #     word += char
        #     if self.tree.search(word):
        #         if self.minExtraChar(s[])
        #         print(f'{word = } exists')
        #         word = ""
        #         continue
        #     if not self.tree.starts_with(word):
        #         # print()
        #         unused += len(word)
        #         word = ""
        #         continue
        # print(f'{word = }')
        # print(f'{unused = }')
        # return unused

