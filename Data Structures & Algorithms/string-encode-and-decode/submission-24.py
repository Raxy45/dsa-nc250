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
            current_word_length_str = ''
            while s[i] != '#':
                current_word_length_str += s[i]
                i += 1
                print(current_word_length_str)
            print('pointer i', i)
            current_word_length = int(current_word_length_str)
            i = i+1
            print(current_word_length)
            word = s[i:i+current_word_length]
            print(word)
            decoded_word_list.append(word)
            print(decoded_word_list, i)

            i = i+current_word_length
        return decoded_word_list
        
