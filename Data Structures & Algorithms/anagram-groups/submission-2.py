class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for st in strs:
            temp= [0] * 26
            for i in range(len(st)):
                temp[ord(st[i]) - ord('a')] += 1
            ans[tuple(temp)].append(st)
        return list(ans.values())

        # 1. Iterate over all strs
        # 2. Build FreqMap of each strs
        # 3. In the dict