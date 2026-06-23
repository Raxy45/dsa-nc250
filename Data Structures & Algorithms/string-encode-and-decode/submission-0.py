class Solution:

    def encode(self, strs: List[str]) -> str:
        return ' '.join(strs)
        # return 'yash'

    def decode(self, s: str) -> List[str]:
        return s.split(' ')