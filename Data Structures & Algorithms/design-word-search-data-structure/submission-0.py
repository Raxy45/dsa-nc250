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

    def search_path(self, word, curr):
        i = 0
        while i < len(word):
            print('searching', word[i],'in curr', curr.children)
            if word[i] != '.':
                if word[i] not in curr.children:
                    return False
                
                curr = curr.children[word[i]]
                i += 1
                if i<len(word):
                    print('found match for', word[i], 'moving char ahead by one', curr.children)
                continue
            
            i += 1
            if i == len(word):
                return len(curr.children) > 0
            
            print('encountered ".", searching', word[i], 'in all children of curr')
            for child in curr.children:
                # if word[i] not in curr.children[child].children:
                #     continue
                # curr = curr.children[child]
                # return self.search_path(word[i:], curr)
                if self.search_path(word[i:], curr.children[child]):
                    return True
            return False
        return curr.eof

    def search(self, word: str) -> bool:
        return self.search_path(word, self.root)


        
