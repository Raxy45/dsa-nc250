class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q, visited, count = deque(), set(), 0
        wLSet = set(wordList)
        q.append(beginWord)

        while q:
            for _ in range(len(q)):
                print(q, count)
                node = q.popleft()
                if node == endWord:
                    return count+1
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

            count += 1
            
        return 0