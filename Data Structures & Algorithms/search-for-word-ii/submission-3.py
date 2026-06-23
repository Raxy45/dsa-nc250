class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.eow = True
    
class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def search(r, c, curr, seen):
            nonlocal word
            if (r<0 or r==len(board)) or (c<0 or c==len(board[r])) or (r,c) in seen:
                return False

            if board[r][c] not in curr.children:
                return False

            self.word += board[r][c]
            seen.add((r, c))
            if curr.children[board[r][c]].eow:
                curr.children[board[r][c]].eow = False
                self.ans.append(self.word)

            search(r, c+1, curr.children[board[r][c]], seen)
            search(r+1, c, curr.children[board[r][c]], seen)
            search(r, c-1, curr.children[board[r][c]], seen)
            search(r-1, c, curr.children[board[r][c]], seen)


            seen.remove((r,c))
            self.word = self.word[:len(self.word)-1]


        trie = Trie()
        for word in words:
            trie.insert(word)
            
        trie_root = trie.root
        self.ans = []
        self.word = ""
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] not in trie_root.children:
                    continue
                seen = set()
                self.word = ""
                search(r, c, trie_root, seen)
                


        return self.ans