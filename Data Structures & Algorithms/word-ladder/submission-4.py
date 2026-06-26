class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def get_diff(w1, w2):
            w1s = defaultdict(int)
            for i in range(len(w1)):
                w1s[w1[i]] += 1
                if w1s[w1[i]] == 0:
                    del w1s[w1[i]]
                w1s[w2[i]] -= 1
                if w1s[w2[i]] == 0:
                    del w1s[w2[i]]
            #     print(w1s, i)
            # print(w1s, w1, w2)
            # print(';l;;lll')
        
            if len(w1s)>2: return False
            for _, diff in w1s.items():
                if abs(diff)>1: return False
            return True
        q = deque([(beginWord, 1)])
        visited = set()
        while q:
            # print('q', q)
            curr_word, curr_transformation = q.popleft()
            # print('curr word, transform_cost', curr_word, curr_transformation)
            if curr_word == endWord:
                return curr_transformation
            for w in wordList:
                if w not in visited and get_diff(curr_word, w):
                    q.append((w, curr_transformation+1))
                    visited.add(w)
        return 0