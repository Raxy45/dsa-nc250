class Trie:
    def __init__(self, char=None, eow=False):
        self.children = {}
        self.char = char
        self.eow = eow
    
    def add_word(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie(char)
            curr = curr.children[char]
        curr.eow = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.add_word(word)    
        
        output = []
        R, C = len(board), len(board[0])
        def dfs(r, c, curr, visited, word):
            if r<0 or r==R or c<0 or c==C or (r,c) in visited or board[r][c] not in curr.children:
                return 
            
            char = board[r][c]
            word += board[r][c]
            visited.add((r,c))
            if curr.children[char].eow:
                output.append(word)
            
            dfs(r, c+1, curr.children[char], visited, word)
            dfs(r+1, c, curr.children[char], visited, word)
            dfs(r, c-1, curr.children[char], visited, word)
            dfs(r-1, c, curr.children[char], visited, word)

            visited.remove((r, c))
            word = word[:len(word)]

        for r in range(R):
            for c in range(C):
                if board[r][c] in trie.children:
                    dfs(r, c, trie, set(), "")
        return output