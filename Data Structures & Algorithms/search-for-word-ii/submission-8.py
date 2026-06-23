class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        ans = []
        R, C = len(board), len(board[0])
        def dfs(r, c, curr, wd):
            nonlocal ans
            # print(r, c, wd)
            if r==R or c==C or min(r, c)<0: return 0
            if board[r][c] == '#': return 0

            if curr.isWord: 
                # print('added',wd,'to ans')
                curr.isWord=False
                ans.append("".join(wd))
            
            if board[r][c] not in curr.children:
                return 0
            
            curr_char = board[r][c]
            board[r][c] = '#'
            wd.append(curr_char)
            rhs = dfs(r, c+1, curr.children[curr_char], wd)
            bottom = dfs(r+1, c, curr.children[curr_char], wd)
            lhs = dfs(r, c-1, curr.children[curr_char], wd)
            top = dfs(r-1, c, curr.children[curr_char], wd)
            board[r][c] = curr_char
            wd.pop()
        
        for i in range(R):
            for j in range(C):
                if board[i][j] in trie.root.children:
                    dfs(i, j, trie.root, [])
        return ans