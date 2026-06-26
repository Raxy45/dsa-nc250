class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([])
        visited = set()
        regex_map = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                regex_map[w[:i] + '*' + w[i+1:]].append(w)
        
        q.append((beginWord, 1))
        visited.add(beginWord)
        while q:
            word, level = q.popleft()
            if word == endWord: return level
            for i in range(len(word)):
                curr_regex = word[:i] + '*' + word[i+1:]
                for matching_words in regex_map[curr_regex]:
                    if matching_words not in visited:
                        q.append((matching_words, level+1))
                        visited.add(matching_words)
                regex_map[curr_regex] = []
        return 0



    def ladderLengthME(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def get_diff(w1, w2):
            diff = 0
            for i in range(len(w1)):
                if w1[i] == w2[i]:
                    continue
                if diff >0:
                    return False
                diff += 1
            return True
                
        q = deque([(beginWord, 1)])
        visited = set()
        while q:
            curr_word, curr_transformation = q.popleft()
            if curr_word == endWord:
                return curr_transformation
            for w in wordList:
                if w not in visited and get_diff(curr_word, w):
                    q.append((w, curr_transformation+1))
                    visited.add(w)
        return 0