class Solution:
    def encode(self, strs: List[str]) -> str:
        encode = ""
        for string in strs:
            str_len = str(len(string))
            encode += str_len + "@" + string
        return encode

    def decode(self, encode: str) -> List[str]:
        decoded_strs = []
        k = 0
        
        while k < len(encode):

            j = k
            while encode[j] != "@":
                j += 1
            
            curr_word_len = int(encode[k:j])
            
            curr_word = encode[j + 1 : j + 1 + curr_word_len]
            decoded_strs.append(curr_word)
            
            k = j + 1 + curr_word_len
            
        return decoded_strs