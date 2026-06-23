class TrieNode:
    def __init__(self):
        self.eof=False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.eof = True

    def search_path(self, idx, curr, word):
        for i in range(idx, len(word)):
            if word[i] != '.':
                if word[i] not in curr.children:
                    return False
                
                curr = curr.children[word[i]]
                continue

            for child in curr.children:
                if self.search_path(i+1, curr.children[child], word):
                    return True
            return False
        return curr.eof
                

    def search(self, word: str) -> bool:
        return self.search_path(0, self.root, word)


        
