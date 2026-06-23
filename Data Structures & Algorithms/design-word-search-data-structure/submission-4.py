class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.eow = True

    def search_path(self, word, curr):
        print('searching', word)
        for i in range(len(word)):
            char = word[i]
            if char != '.':
                if char not in curr.children:
                    return False
                curr = curr.children[char]
                continue
            # char is wild card
            print('wild card',i, word)
            for child in curr.children:
                if self.search_path(word[i+1:], curr.children[child]):
                    return True
            return False
        return curr.eow
    def search(self, word: str) -> bool:
        return self.search_path(word, self.root)
