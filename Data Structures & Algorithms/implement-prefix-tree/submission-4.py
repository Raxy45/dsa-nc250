class TrieNode:
    def __init__(self, char=None, next=None, eow=False):
        self.char = char
        self.eow = eow
        self.next = next
        self.children = defaultdict(TrieNode)

class PrefixTree:

    def __init__(self):
        self.parent = TrieNode()

    def insert(self, word: str) -> None:
        i = 0
        if not word: return

        curr = self.parent
        while i<len(word):
            current_char = word[i]
            if current_char not in curr.children:
                new_node = TrieNode(current_char)
                curr.children[current_char] = new_node #new linkage established
            
            curr = curr.children[current_char]
            i += 1
        curr.eow = True

    def search(self, word: str) -> bool:
        i = 0
        if not word: return

        curr = self.parent
        while i<len(word):
            current_char = word[i]
            if current_char not in curr.children: return False
            curr = curr.children[current_char]
            i += 1

        return curr.eow

    def startsWith(self, prefix: str) -> bool:
        i = 0
        if not prefix: return

        curr = self.parent
        while i<len(prefix):
            current_char = prefix[i]
            if current_char not in curr.children: return False
            curr = curr.children[current_char]
            i += 1

        return True
        
        