class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s))
            enc += '#'
            enc += s
        print(enc)
        return enc
    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0
        print(s)
        while i<len(s):
            s_len = int(s[i])
            i += 2
            print('adding s',s[i:i+s_len])
            dec.append(s[i:i+s_len])
            i = i+s_len
        return dec