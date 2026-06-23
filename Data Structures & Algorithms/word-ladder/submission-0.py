class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q, visited, count = deque(), set(), 1
        wLSet = set(wordList)
        q.append(beginWord)

        while q:
            print(q)
            node = q.popleft()
            if node == endWord:
                return count
            found_match = False
            for i in range(len(node)):
                # iterating over each char in popped word

                # current char to be replaced
                char = node[i]
                for updated_char in 'abcdefghijklmnopqrstuvwxyz':
                    if updated_char == char: continue
                    updated_word = node[:i] + updated_char + node[i+1:]
                    # print('updated_word', updated_word)
                    if updated_word in visited: continue
                    if updated_word in wLSet:
                        print('found match', updated_word)
                        visited.add(updated_word)
                        q.append(updated_word)
                        found_match = True

            if found_match:
                count += 1
            
        return 0