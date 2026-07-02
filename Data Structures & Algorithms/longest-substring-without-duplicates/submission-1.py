from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) >= 2:
            left = 0
            right = 1
            current_window = set()
            current_window.add(s[left])
            maxl = 0

            while right < len(s):

                if s[right] not in current_window:
                    current_window.add(s[right])
                    right += 1
                    maxl = max(maxl, len(current_window))
                    continue
                
                else:
                    while s[right] in current_window :
                        current_window.discard(s[left])
                        left += 1
            return maxl
        else:
            return len(s)


