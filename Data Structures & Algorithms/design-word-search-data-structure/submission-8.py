class TrieNode:
    def __init__(self, char=None, eow=False):
        self.char = char
        self.eow = eow
        self.children = [TrieNode for _ in range(26)]
        print('ss')
        print(self.children[0].char)

class WordDictionary:

    def __init__(self):
        self.parent = TrieNode()

    def idx(self, char):
        return ord(char) - ord('a')

    def addWord(self, word: str) -> None:
        if not word: return
        i = 0
        curr = self.parent
        while curr and i<len(word):
            if word[i] not in curr.children:
                new_node = TrieNode(word[i])
                curr.children[self.idx(word[i])] = new_node
            
            curr = curr.children[self.idx(word[i])]
            i += 1
        
        curr.eow = True

    def search_rec(self, word, curr):
        i = 0
        print(i, word)
        while curr and i<len(word):
            curr_char = word[i]
            if curr_char !='.':
                if curr_char not in curr.children: return False
                curr = curr.children[self.idx(curr_char)]
                i += 1
                continue
            # now curr char is '.' -> search all levels
            print(curr, word[i])
            print(curr.children)
            for curr_child in curr.children:
                if curr_child:
                    # non None char
                    if self.search_rec( word[i:], curr_child): return True
        if i==len(word): return True
        return False
            
    def search(self, word: str) -> bool:
        return self.search_rec(word, self.parent)
