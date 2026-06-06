class TrieNode:
    def __init__(self, char=None, eow=False):
        self.char = char
        self.eow = eow
        self.children = [None] * 26

class WordDictionary:

    def __init__(self):
        self.parent = TrieNode()
        self.j=0

    def idx(self, char):
        return ord(char) - ord('a')

    def addWord(self, word: str) -> None:
        if not word: return
        i = 0
        curr = self.parent
        while curr and i<len(word):
            if not curr.children[self.idx(word[i])]:
                new_node = TrieNode(word[i])
                curr.children[self.idx(word[i])] = new_node
            
            curr = curr.children[self.idx(word[i])]
            i += 1
        
        curr.eow = True

    def search_rec(self, word, curr):
        i = 0
        while curr and i<len(word):
            curr_char = word[i]
            if curr_char !='.':
                if not curr.children[self.idx(curr_char)]: return False
                curr = curr.children[self.idx(curr_char)]
                i += 1
                continue
            # now curr char is '.' -> search all +1 levels of curr
            for curr_child in curr.children:
                # print(curr_child, 'aasss')
                if curr_child:
                    # non None char
                    # print('non none', curr_child.char)
                    if self.search_rec(word[i+1:], curr_child): return True
            return False
        if i==len(word) and curr.eow: return True
        return False
            
    def search(self, word: str) -> bool:
        return self.search_rec(word, self.parent)
