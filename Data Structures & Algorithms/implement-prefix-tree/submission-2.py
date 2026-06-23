class TrieNode:
    def __init__(self, char='0', eow=False):
        self.char = char
        self.eow=eow
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.base = {}

    def insert(self, word: str) -> None:
        if word[0] not in self.base:
            self.base[word[0]] = TrieNode(word[0])
        prev = self.base[word[0]]

        for i in range(1, len(word)):
            if word[i] not in prev.children:
                node = TrieNode(word[i])
                prev.children[word[i]] = node
            else:
                node = prev.children[word[i]]
            prev = node
        prev.eow = True
            

    def search(self, word: str) -> bool:
        if word[0] not in self.base: return False
        trie = self.base[word[0]]
        for i in range(1, len(word)):
            if word[i] not in trie.children:
                print(word[i],'not a child of', trie)
                return False
            trie = trie.children[word[i]]
        print('eow', trie.char)
        return trie.eow

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] not in self.base: return False
        trie = self.base[prefix[0]]
        for i in range(1, len(prefix)):
            if prefix[i] not in trie.children:
                return False
            trie = trie.children[prefix[i]]
        return True
        