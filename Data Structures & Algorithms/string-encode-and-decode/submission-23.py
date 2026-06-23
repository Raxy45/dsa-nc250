class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in strs:
            current_len = len(i)
            updated_word = f'{current_len}#{i}'
            encoded_str += updated_word
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_word_list = []
        i = 0
        while i < len(s):
            print(s[i])
            current_word_length = int(s[i])
            print(current_word_length)
            word = s[i+2:i+current_word_length+2]
            print(word)
            decoded_word_list.append(word)
            print(decoded_word_list, i)

            i = i + current_word_length + 2
        return decoded_word_list
        
