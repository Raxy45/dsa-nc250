class Solution:

    def encode(self, strs: List[str]) -> str:
        print(strs, type(strs), len(strs))
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            print('in here', strs[0].strip(), 'c')
            return strs[0]
        print(' '.join(strs))
        return ' '.join(strs)
        # return 'yash'

    def decode(self, s: str) -> List[str]:
        print('decode', s, 'yash')
        print(len(s))
        if len(s) == 0:
            return []
        if ' ' not in s:
            return []
        return s.split(' ')