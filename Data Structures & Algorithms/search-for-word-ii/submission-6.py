class Trie:
    def __init__(self, char=None, eow=False):
        self.children = {}
        self.char = char
        self.eow = eow
        self.word = ""
    
    def add_word(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie(char)
            curr = curr.children[char]
        curr.eow = True
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.add_word(word)    
        
        output = []
        R, C = len(board), len(board[0])
        def dfs(r, c, curr):
            if r<0 or r==R or c<0 or c==C or board[r][c]=='#' or board[r][c] not in curr.children:
                return 
            
            char = board[r][c]
            board[r][c] = '#'
            if curr.children[char].eow:
                curr.children[char].eow = False
                output.append(curr.children[char].word)
            
            dfs(r, c+1, curr.children[char])
            dfs(r+1, c, curr.children[char])
            dfs(r, c-1, curr.children[char])
            dfs(r-1, c, curr.children[char])

            board[r][c] = char

        for r in range(R):
            for c in range(C):
                if board[r][c] in trie.children:
                    dfs(r, c, trie)
        return output