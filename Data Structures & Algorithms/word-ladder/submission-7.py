class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
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