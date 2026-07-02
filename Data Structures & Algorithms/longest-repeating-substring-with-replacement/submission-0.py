class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        left = 0
        right = 0
        maxl = 0

        while right < len(s):

            char_count[s[right]] = 1 + char_count.get(s[right], 0)
            win_size = right - left + 1

            max_freq = max(char_count.values())

            while (right - left + 1) - max(char_count.values()) > k:

                char_count[s[left]] -= 1
                left += 1
            
            maxl = max(maxl, right - left + 1)
            right += 1
            print(char_count)

            
        return maxl