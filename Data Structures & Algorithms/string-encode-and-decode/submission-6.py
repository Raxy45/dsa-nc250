class Solution:

    def encode(self, strs: List[str]) -> str:
        print(strs, type(strs), len(strs))
        if len(strs) == 0:
            return ''
        print(' '.join(strs))
        return ' '.join(strs)
        # return 'yash'

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        return s.split(' ')