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
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        self.tree = Tree()
        for word in dictionary:
            self.tree.insert(word)

        word = ""
        unused = 0
        for char in s:
            word += char
            if self.tree.search(word):
                word = ""
                continue
            if not self.tree.starts_with(word):
                # print()
                unused += len(word)
                word = ""
                continue
        print(f'{word = }')
        print(f'{unused = }')
        return unused

