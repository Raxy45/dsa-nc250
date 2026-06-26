class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([])
        visited = set()

        def get_pattern(w):
            temp_pattern = []
            for i in range(len(w)):
                temp = w[:i] + '*' + w[i+1:]
                if temp in visited:
                    continue
                visited.add(temp)
                temp_pattern.append((temp, w))
            return temp_pattern

        def get_diff(w, regex):
            for i in range(len(w)):
                if w[:i] + '*' + w[i+1:] == regex:
                    return True
            return False

        q.extend(get_pattern(beginWord))
        level = 1
        
        while q:
            for _ in range(len(q)):
                current_regex, curr_w = q.popleft()
                if curr_w == endWord: return level
                for w in wordList:
                    if get_diff(w, current_regex):
                        q.extend(get_pattern(w))
            level += 1
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