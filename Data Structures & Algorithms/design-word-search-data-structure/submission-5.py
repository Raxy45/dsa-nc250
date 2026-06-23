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
                # skip current char in word, as it is anyways wild card "."
                # then for current child, go to current child's child example if word is day,dog.
                # to find is d*g -> 
                # 1. d is matched to to next char which in word which is '*'
                # 2. Now, Go to next char in word(which is g), iterate over all children of d -> a, o
                # 3. Check if g is child of a or 0
                if self.search_path(word[i+1:], curr.children[child]):
                    return True
            return False
        return curr.eow
    def search(self, word: str) -> bool:
        return self.search_path(word, self.root)
